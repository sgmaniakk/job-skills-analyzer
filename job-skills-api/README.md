# Job Skills Analyzer - Backend API

A FastAPI-based backend service that uses NLP to extract and analyze technical skills from job descriptions.

## Tech Stack

- **FastAPI** - Modern Python web framework
- **spaCy** - Natural Language Processing library
- **PostgreSQL** - Database
- **SQLAlchemy** - ORM
- **Alembic** - Database migrations

## Setup

### Prerequisites

- Python 3.9+
- PostgreSQL

### Installation

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download spaCy language model:
```bash
python -m spacy download en_core_web_lg
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your database credentials
```

5. Run database migrations:
```bash
alembic upgrade head
```

### Running the Server

```bash
uvicorn app.main:app --reload --port 8000
```

API documentation will be available at: http://localhost:8000/docs

## API Endpoints

- `GET /health` - Health check
- `POST /api/v1/analysis/analyze` - Analyze single job description
- `POST /api/v1/analysis/batch` - Analyze multiple job descriptions

## Testing

```bash
pytest
```

## Project Structure

```
app/
├── main.py              # FastAPI application entry point
├── config.py            # Configuration management
├── database.py          # Database connection
├── models/              # SQLAlchemy models
├── schemas/             # Pydantic schemas
├── api/
│   ├── deps.py          # Dependencies
│   └── routes/          # API routes
├── services/            # Business logic
│   ├── nlp_service.py
│   └── skills_extractor.py
└── core/                # Core utilities
    └── skills_database.py
```
