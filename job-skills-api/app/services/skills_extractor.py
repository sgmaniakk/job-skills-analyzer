"""
Skills Extractor using spaCy NLP.
Extracts technical skills from job descriptions using:
1. Pattern matching against curated skills database
2. Entity recognition for technical terms
3. Contextual extraction based on keywords
"""

import spacy
from spacy.matcher import PhraseMatcher
from typing import List, Dict
from collections import Counter
import re

from app.core.skills_database import SKILLS_DATABASE, get_category_for_skill


class SkillsExtractor:
    """Extract and categorize skills from job descriptions using NLP"""

    def __init__(self):
        """Initialize spaCy model and phrase matcher"""
        print("Loading spaCy model...")
        self.nlp = spacy.load("en_core_web_lg")
        self.phrase_matcher = PhraseMatcher(self.nlp.vocab, attr="LOWER")
        self._initialize_patterns()
        print("Skills extractor initialized successfully!")

    def _initialize_patterns(self):
        """Initialize phrase matcher with all skills from database"""
        for category, skills in SKILLS_DATABASE.items():
            # Create patterns for each skill
            patterns = [self.nlp.make_doc(skill) for skill in skills]
            self.phrase_matcher.add(category, patterns)

    def extract_skills(self, text: str) -> List[Dict]:
        """
        Extract skills from job description text.

        Args:
            text: Job description text

        Returns:
            List of skill dictionaries with name, count, category, and confidence
        """
        # Process text with spaCy
        doc = self.nlp(text)

        # 1. Pattern matching (high confidence)
        pattern_skills = self._find_pattern_matches(doc)

        # 2. Entity recognition for tech terms (medium confidence)
        entity_skills = self._extract_entities(doc)

        # 3. Contextual extraction (lower confidence)
        contextual_skills = self._extract_contextual_skills(doc)

        # Merge and deduplicate skills
        all_skills = self._merge_skills(pattern_skills, entity_skills, contextual_skills)

        # Convert to list format
        skills_list = []
        for skill_name, skill_data in all_skills.items():
            skills_list.append({
                "name": skill_name,
                "count": skill_data["count"],
                "category": skill_data["category"],
                "confidence": skill_data["confidence"],
            })

        # Sort by count (descending) then by confidence (descending)
        skills_list.sort(key=lambda x: (x["count"], x["confidence"]), reverse=True)

        return skills_list

    def _find_pattern_matches(self, doc) -> Dict:
        """Find exact and fuzzy matches using phrase matcher"""
        skills = {}
        matches = self.phrase_matcher(doc)

        for match_id, start, end in matches:
            # Get the matched span
            span = doc[start:end]
            skill_name = span.text

            # Normalize skill name (title case)
            skill_name = self._normalize_skill_name(skill_name)

            # Get category from match_id
            category = self.nlp.vocab.strings[match_id]

            if skill_name not in skills:
                skills[skill_name] = {
                    "count": 0,
                    "category": category,
                    "confidence": 0.95,  # High confidence for exact matches
                }
            skills[skill_name]["count"] += 1

        return skills

    def _extract_entities(self, doc) -> Dict:
        """Extract technical entities using NER"""
        skills = {}

        for ent in doc.ents:
            # Focus on entities likely to be technical skills
            if ent.label_ in ["PRODUCT", "ORG", "GPE"]:
                skill_name = self._normalize_skill_name(ent.text)

                # Check if it matches known skills (case-insensitive)
                category = get_category_for_skill(skill_name)

                if category != "other":  # Only include if it's a known skill
                    if skill_name not in skills:
                        skills[skill_name] = {
                            "count": 0,
                            "category": category,
                            "confidence": 0.75,  # Medium-high confidence
                        }
                    skills[skill_name]["count"] += 1

        return skills

    def _extract_contextual_skills(self, doc) -> Dict:
        """Extract skills from contextual phrases"""
        skills = {}

        # Keywords that often precede skills
        skill_keywords = [
            "experience with",
            "proficient in",
            "knowledge of",
            "expertise in",
            "skilled in",
            "familiar with",
            "working with",
            "understanding of",
        ]

        text_lower = doc.text.lower()

        # Find skill mentions near keywords
        for keyword in skill_keywords:
            # Find all occurrences of the keyword
            for match in re.finditer(re.escape(keyword), text_lower):
                start_idx = match.end()
                # Look at the next 50 characters
                context = text_lower[start_idx:start_idx + 50]

                # Extract potential skills (words that might be skills)
                words = re.findall(r'\b[A-Za-z][A-Za-z0-9+#.]*\b', context)

                for word in words[:5]:  # Limit to first 5 words after keyword
                    # Check if it's a known skill
                    category = get_category_for_skill(word)
                    if category != "other":
                        skill_name = self._normalize_skill_name(word)
                        if skill_name not in skills:
                            skills[skill_name] = {
                                "count": 0,
                                "category": category,
                                "confidence": 0.60,  # Lower confidence for contextual
                            }
                        skills[skill_name]["count"] += 1

        return skills

    def _merge_skills(self, *skill_dicts) -> Dict:
        """Merge multiple skill dictionaries, keeping highest confidence and summing counts"""
        merged = {}

        for skill_dict in skill_dicts:
            for skill_name, skill_data in skill_dict.items():
                if skill_name not in merged:
                    merged[skill_name] = skill_data.copy()
                else:
                    # Sum counts
                    merged[skill_name]["count"] += skill_data["count"]
                    # Keep highest confidence
                    merged[skill_name]["confidence"] = max(
                        merged[skill_name]["confidence"],
                        skill_data["confidence"]
                    )

        return merged

    def _normalize_skill_name(self, skill_name: str) -> str:
        """Normalize skill name for consistency"""
        # Remove extra whitespace
        skill_name = " ".join(skill_name.split())

        # Handle special cases
        skill_name_lower = skill_name.lower()

        # Common normalizations
        normalizations = {
            "react.js": "React",
            "reactjs": "React",
            "vue.js": "Vue",
            "vuejs": "Vue",
            "next.js": "Next.js",
            "nextjs": "Next.js",
            "node.js": "Node.js",
            "nodejs": "Node.js",
            "javascript": "JavaScript",
            "typescript": "TypeScript",
            "postgresql": "PostgreSQL",
            "mongodb": "MongoDB",
            "mysql": "MySQL",
            "aws": "AWS",
            "gcp": "GCP",
            "k8s": "Kubernetes",
        }

        return normalizations.get(skill_name_lower, skill_name)
