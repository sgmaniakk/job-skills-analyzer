from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime
from uuid import UUID, uuid4


class SkillBase(BaseModel):
    """Base schema for a detected skill"""
    name: str
    count: int = 1
    category: str
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score between 0 and 1")


class Skill(SkillBase):
    """Skill with ID"""
    id: UUID = Field(default_factory=uuid4)


class AnalysisCreate(BaseModel):
    """Schema for creating a new job analysis"""
    job_description: str = Field(
        min_length=50,
        description="The job description text to analyze"
    )
    title: Optional[str] = Field(
        None,
        max_length=255,
        description="Optional job title"
    )


class AnalysisResponse(BaseModel):
    """Schema for single job analysis response"""
    id: UUID = Field(default_factory=uuid4)
    title: Optional[str]
    analyzed_at: datetime = Field(default_factory=datetime.utcnow)
    skills: List[Skill]
    total_skills_found: int
    categories: Dict[str, int] = Field(
        description="Count of skills per category"
    )


class BatchAnalysisRequest(BaseModel):
    """Schema for analyzing multiple jobs"""
    jobs: List[AnalysisCreate] = Field(
        min_length=1,
        max_length=50,
        description="List of job descriptions to analyze (max 50)"
    )


class AggregatedSkill(BaseModel):
    """Schema for aggregated skill across multiple jobs"""
    name: str
    total_count: int = Field(description="Total occurrences across all jobs")
    appeared_in_jobs: int = Field(description="Number of jobs this skill appeared in")
    percentage: float = Field(
        ge=0.0,
        le=100.0,
        description="Percentage of jobs containing this skill"
    )
    category: str


class BatchAnalysisResponse(BaseModel):
    """Schema for batch analysis response"""
    id: UUID = Field(default_factory=uuid4)
    analyzed_at: datetime = Field(default_factory=datetime.utcnow)
    total_jobs: int
    aggregated_skills: List[AggregatedSkill]
    individual_analyses: List[AnalysisResponse]
    top_skills: List[AggregatedSkill] = Field(
        description="Top 20 most common skills"
    )
    category_breakdown: Dict[str, int] = Field(
        description="Total skills per category across all jobs"
    )
