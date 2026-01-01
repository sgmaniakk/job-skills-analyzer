# Job Skills Analyzer

A full-stack web application that analyzes job descriptions to extract and rank technical skills using Natural Language Processing (NLP).

## Features

- Extract technical skills from job descriptions using spaCy NLP
- Analyze single or multiple job postings
- Visualize skill frequency with interactive charts
- Categorize skills (programming languages, frameworks, databases, tools, etc.)
- Track skill trends across multiple job postings

## Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **spaCy** - Industrial-strength NLP library
- **PostgreSQL** - Relational database
- **SQLAlchemy** - Python ORM
- **Alembic** - Database migrations

### Frontend
- **React** - UI library
- **TypeScript** - Type-safe JavaScript
- **Vite** - Build tool
- **Recharts** - Data visualization
- **Tailwind CSS** - Utility-first CSS framework

### Deployment
- **Railway** - Backend hosting
- **Vercel** - Frontend hosting

## Project Structure

```
job-skills-analyzer/
├── job-skills-api/          # FastAPI backend
│   ├── app/
│   │   ├── api/             # API routes
│   │   ├── core/            # Core utilities
│   │   ├── models/          # SQLAlchemy models
│   │   ├── schemas/         # Pydantic schemas
│   │   └── services/        # Business logic (NLP)
│   └── tests/
└── job-skills-ui/           # React frontend (coming soon)
```

## Getting Started

### Backend Setup

```bash
cd job-skills-api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_lg
uvicorn app.main:app --reload
```

API docs: http://localhost:8000/docs

## Development Status

- [x] Backend project setup
- [x] FastAPI application skeleton
- [x] Configuration management
- [ ] Database models and migrations
- [ ] NLP skill extraction service
- [ ] API endpoints for analysis
- [ ] React frontend setup
- [ ] Data visualization components
- [ ] Deployment

## License

MIT

## Author

Matt Anderson
