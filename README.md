# FastAPI Stage 0 Backend - HNG12 Assignment

[![Python Version](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green)](https://fastapi.tiangolo.com/)
[![Deployed on Render](https://img.shields.io/badge/deploy%20on-Render-46C3D2)](https://render.com)

A public API built with FastAPI for the HNG12 Backend Internship Stage 0. Returns user details and current UTC datetime.

**Live Demo**: Currently Unavailable

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
  - [Prerequisites](#prerequisites)
  - [Local Setup](#local-setup)
- [API Documentation](#api-documentation)
  - [Endpoint](#endpoint)
  - [Response Format](#response-format)
- [Deployment](#deployment)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Features

- **Dynamic datetime**: Returns current UTC datetime in ISO 8601 format.
- **CORS Support**: Preconfigured middleware for cross-origin requests.
- **Auto-Generated Docs**: Interactive Swagger/OpenAPI documentation at `/docs`.
- **Scalable**: Ready for deployment on Render (or similar platforms).

---

## Tech Stack

- **Language**: Python 3.12
- **Framework**: FastAPI
- **Server**: Uvicorn
- **Deployment**: Render
- **Version Control**: Git & GitHub

---

## Quick Start

### Prerequisites

- Python 3.11+
- Git
- Render account (free tier)

### Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Joe-encodes/fastapi-project.git
   cd fastapi-project
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv  # Create virtual environment
   source venv/bin/activate  # Activate on Linux/macOS
   venv\Scripts\activate  # Activate on Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the API locally**:
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API**:
   - API Root: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Documentation

### Endpoint

- **GET /** – Returns a JSON object with user details and current UTC datetime.

### Response Format

```json
{
  "email": "joseph.adamu.it@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Joe-encodes/fastapi-project"
}
```

---

## Deployment

### Deploy on Render

1. **Connect your GitHub repo to Render**
2. **Configure settings**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port 10000`
3. **Deploy and monitor logs in the Render dashboard**

---

## Testing

### Manual Testing

```bash
curl https://your-app-name.onrender.com
```

### Automated Testing (with pytest)

#### `tests/test_main.py`

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "email" in response.json()
```

### Run tests:

```bash
pytest -v
```

---

## Contributing

Pull requests are welcome! For major changes, open an issue first.

---

## License

GNU

---

## Acknowledgments

- HNG Internship for the project brief.
- FastAPI Documentation for best practices.

---

## Contact

- **Email**: joseph.adamu.it@gmail.com  
- **GitHub**: https://github.com/Joe-encodes
- **LinkedIn**: linkedin.com/in/joseph-adamu-it

## To Hire Other Developers like me

- **Python**: https://hng.tech/hire/python-developers
