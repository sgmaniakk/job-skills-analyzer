"""
NLP Service wrapper for skills extraction.
Provides a high-level interface for analyzing job descriptions.
"""

import re
from typing import List, Dict
from app.services.skills_extractor import SkillsExtractor


class NLPService:
    """Service for NLP-based job description analysis"""

    _instance = None  # Singleton instance

    def __new__(cls):
        """Singleton pattern to avoid loading spaCy model multiple times"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """Initialize the NLP service (only once due to singleton)"""
        if not self._initialized:
            self.skills_extractor = SkillsExtractor()
            self._initialized = True

    def analyze_job_description(self, job_description: str) -> Dict:
        """
        Analyze a single job description and extract skills.

        Args:
            job_description: The job description text

        Returns:
            Dictionary with extracted skills and statistics
        """
        # Preprocess text
        cleaned_text = self._preprocess_text(job_description)

        # Extract skills
        skills = self.skills_extractor.extract_skills(cleaned_text)

        # Calculate category breakdown
        category_counts = {}
        for skill in skills:
            category = skill["category"]
            category_counts[category] = category_counts.get(category, 0) + 1

        return {
            "skills": skills,
            "total_skills_found": len(skills),
            "categories": category_counts,
        }

    def analyze_multiple_jobs(self, job_descriptions: List[str]) -> Dict:
        """
        Analyze multiple job descriptions and aggregate results.

        Args:
            job_descriptions: List of job description texts

        Returns:
            Dictionary with aggregated skills across all jobs
        """
        all_analyses = []
        skill_aggregation = {}  # skill_name -> {total_count, job_count, category}

        # Analyze each job
        for job_text in job_descriptions:
            analysis = self.analyze_job_description(job_text)
            all_analyses.append(analysis)

            # Track which skills appeared in this job (for percentage calculation)
            skills_in_this_job = set()

            # Aggregate skills
            for skill in analysis["skills"]:
                skill_name = skill["name"]
                skills_in_this_job.add(skill_name)

                if skill_name not in skill_aggregation:
                    skill_aggregation[skill_name] = {
                        "total_count": 0,
                        "job_count": 0,
                        "category": skill["category"],
                    }

                skill_aggregation[skill_name]["total_count"] += skill["count"]

            # Increment job count for each unique skill
            for skill_name in skills_in_this_job:
                skill_aggregation[skill_name]["job_count"] += 1

        # Convert to list with percentages
        total_jobs = len(job_descriptions)
        aggregated_skills = []

        for skill_name, data in skill_aggregation.items():
            percentage = (data["job_count"] / total_jobs) * 100
            aggregated_skills.append({
                "name": skill_name,
                "total_count": data["total_count"],
                "appeared_in_jobs": data["job_count"],
                "percentage": round(percentage, 1),
                "category": data["category"],
            })

        # Sort by total_count descending
        aggregated_skills.sort(key=lambda x: x["total_count"], reverse=True)

        # Get top 20 skills
        top_skills = aggregated_skills[:20]

        # Calculate category breakdown across all jobs
        category_breakdown = {}
        for skill in aggregated_skills:
            category = skill["category"]
            category_breakdown[category] = category_breakdown.get(category, 0) + 1

        return {
            "aggregated_skills": aggregated_skills,
            "top_skills": top_skills,
            "category_breakdown": category_breakdown,
            "individual_analyses": all_analyses,
        }

    def _preprocess_text(self, text: str) -> str:
        """
        Preprocess job description text.

        Args:
            text: Raw text

        Returns:
            Cleaned text
        """
        # Remove HTML tags if any
        text = re.sub(r'<[^>]+>', '', text)

        # Normalize whitespace
        text = re.sub(r'\s+', ' ', text)

        # Remove special characters but keep alphanumeric, spaces, and common punctuation
        # Keep: letters, numbers, spaces, periods, commas, hyphens, slashes, parentheses, +, #
        text = re.sub(r'[^a-zA-Z0-9\s.,\-/()+#]', '', text)

        # Strip leading/trailing whitespace
        text = text.strip()

        return text
