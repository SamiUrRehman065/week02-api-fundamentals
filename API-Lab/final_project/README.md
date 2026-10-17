# Final Integration Project: REST API Client

## Project Overview
This project consolidates all topics covered across Phases 01 through 05 of the Week 02 API Lab:
- REST API Client-Server interaction
- JSON data processing
- Environment variable credential management (`.env`)
- Comprehensive HTTP status validation (200, 404, 429, 500)
- Network failure, timeout, and connection error handling
- Transition of API operations into AI agent tool interfaces

## Setup and Installation

1. Create a virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2. Configure environment variables (optional):
```bash
# Create .env from template
cp .env.example .env
```

3. Run the API client:
```bash
python src/api_client.py
```

## API Documentation
- **Endpoint**: `https://jsonplaceholder.typicode.com/posts/{id}`
- **HTTP Method**: `GET`
- **Parameters**: `id` (integer)
- **Response Format**: `application/json`
- **Error Handling**: Graceful fallback on 404, 429, 500, timeouts, and network outages.
