"""
API routes for job description analysis.
"""

from fastapi import APIRouter, HTTPException
from datetime import datetime
from uuid import uuid4

from app.schemas.analysis import (
    AnalysisCreate,
    AnalysisResponse,
    BatchAnalysisRequest,
    BatchAnalysisResponse,
    Skill,
    FetchJobRequest,
    FetchJobResponse,
)
from app.services.nlp_service import NLPService
from app.services.job_fetcher import JobFetcher, JobFetchError

router = APIRouter()

# Initialize NLP service (singleton)
nlp_service = NLPService()


@router.post("/analyze", response_model=AnalysisResponse)
def analyze_job(request: AnalysisCreate):
    """
    Analyze a single job description and extract skills.

    Args:
        request: Job description and optional title

    Returns:
        Analysis results with extracted skills and statistics
    """
    try:
        # Analyze job description
        result = nlp_service.analyze_job_description(request.job_description)

        # Convert skills to Pydantic models
        skills = [
            Skill(
                name=skill["name"],
                count=skill["count"],
                category=skill["category"],
                confidence=skill["confidence"],
            )
            for skill in result["skills"]
        ]

        # Create response
        response = AnalysisResponse(
            id=uuid4(),
            title=request.title,
            analyzed_at=datetime.utcnow(),
            skills=skills,
            total_skills_found=result["total_skills_found"],
            categories=result["categories"],
        )

        return response

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing job description: {str(e)}"
        )


@router.post("/batch", response_model=BatchAnalysisResponse)
def analyze_batch(request: BatchAnalysisRequest):
    """
    Analyze multiple job descriptions and aggregate results.

    Args:
        request: List of job descriptions to analyze

    Returns:
        Aggregated analysis results across all jobs
    """
    try:
        # Extract job description texts
        job_texts = [job.job_description for job in request.jobs]

        # Analyze all jobs
        batch_result = nlp_service.analyze_multiple_jobs(job_texts)

        # Convert individual analyses to response models
        individual_analyses = []
        for i, (job, analysis) in enumerate(zip(request.jobs, batch_result["individual_analyses"])):
            skills = [
                Skill(
                    name=skill["name"],
                    count=skill["count"],
                    category=skill["category"],
                    confidence=skill["confidence"],
                )
                for skill in analysis["skills"]
            ]

            individual_analyses.append(
                AnalysisResponse(
                    id=uuid4(),
                    title=job.title,
                    analyzed_at=datetime.utcnow(),
                    skills=skills,
                    total_skills_found=analysis["total_skills_found"],
                    categories=analysis["categories"],
                )
            )

        # Create batch response
        response = BatchAnalysisResponse(
            id=uuid4(),
            analyzed_at=datetime.utcnow(),
            total_jobs=len(request.jobs),
            aggregated_skills=batch_result["aggregated_skills"],
            individual_analyses=individual_analyses,
            top_skills=batch_result["top_skills"],
            category_breakdown=batch_result["category_breakdown"],
        )

        return response

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing batch jobs: {str(e)}"
        )


@router.post("/fetch-job", response_model=FetchJobResponse)
async def fetch_job_from_url(request: FetchJobRequest):
    """
    Fetch job title and description from a job board URL.

    Supports:
    - Greenhouse.io
    - Lever.co
    - LinkedIn (limited)
    - Generic job boards (best-effort)

    Args:
        request: URL to the job posting

    Returns:
        Extracted job title and description
    """
    try:
        result = await JobFetcher.fetch_job(request.url)

        return FetchJobResponse(
            title=result['title'],
            description=result['description'],
            url=request.url
        )

    except JobFetchError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching job from URL: {str(e)}"
        )
