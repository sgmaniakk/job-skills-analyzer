# Job Skills Analyzer - Frontend

A React + TypeScript frontend for analyzing job descriptions and visualizing extracted technical skills.

## Features

- **Job Upload**: Paste job descriptions to analyze
- **Interactive Charts**: Bar chart for top skills, pie chart for category breakdown
- **Sortable Table**: View all extracted skills with filtering by category
- **Data Export**: Download analysis results as JSON
- **Responsive Design**: Works on desktop and mobile devices

## Tech Stack

- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **Tailwind CSS** - Utility-first styling
- **Recharts** - Data visualization
- **Axios** - HTTP client

## Getting Started

### Prerequisites

- Node.js 22+
- Backend API running at http://localhost:8000

### Installation

```bash
# Install dependencies
npm install

# Set up environment variables
cp .env.example .env
# Edit .env to set VITE_API_URL if needed

# Start development server
npm run dev
```

The app will be available at http://localhost:5173

## License

MIT
