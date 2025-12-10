# TIMEWISE - Focus Planner API

A modern REST API for managing and planning focused work sessions.

## Requirements

- Python 3.14+
- pip (package manager)

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/100472330/TIMEWISE.git
cd TIMEWISE

2. **Create a virtual environment:**
python -m venv .venv
source .venv/bin/activate  # on macOS/Linux
# or on Windows:
# .venv\Scripts\activate

3. **Install Dependencies:**
pip install -r requirements.txt

**## Running the Application**
From the project root: uvicorn backend.app.main:app --reload
The API will be available at http://127.0.0.1:8000

Available Endpoints
GET /health - Check API health status
curl http://127.0.0.1:8000/health
Response: {"status":"ok"}

**## Running Tests**
From the project root: pytest -q
For verbose output: pytest -v

**## PROJECT STRUCTURE**
.
├── backend/
│   ├── __init__.py
│   ├── app/
│   │   ├── __init__.py
│   │   └── main.py              # FastAPI application
│   └── tests/
│       ├── conftest.py          # pytest configuration
│       └── test_health.py       # Test suite
├── requirements.txt              # Project dependencies
├── .gitignore                    # Git ignore rules
└── README.md                     # This file

**## MAIN DEPENDENCIES**
FastAPI - Modern, fast web framework for building APIs
Uvicorn - ASGI web server implementation
Pytest - Testing framework
HTTPx - HTTP client for testing

**## DEVELOPMENT**
To contribute to the project:

Create a feature branch: git checkout -b feature/my-feature
Commit your changes: git commit -am 'Add my feature'
Push to the branch: git push origin feature/my-feature
Open a Pull Request

**## LICENCE**
This project is licensed under the MIT License.

**## AUTHOR**
Maria Romero Martin






