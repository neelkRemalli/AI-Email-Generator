# AI Email Generator

A Python AI-powered email generation application built with the OpenAI API.

## Features

- Generate professional emails using AI

- Customize email purpose

- Customize email tone

- Provide key points

- Generate an appropriate subject

- Input validation

- Custom application exceptions

- OpenAI integration

- Request timeout

- Retry handling

- Logging

- Unit testing

- Mocking external API calls

- Environment-based configuration

## Architecture

ai-email-generator/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── api.py
│   ├── exceptions.py
│   ├── utils.py
│   │
│   └── services/
│       ├── __init__.py
│       └── email_generator_service.py
│
├── tests/
│   ├── test_api.py
│   └── test_email_generator_service.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

The application follows a simple layered architecture:

```text
User
 │
 ▼
main.py
 │
 ▼
email_generator_service.py
 │
 ▼
api.py
 │
 ▼
OpenAI

## Installation

python -m pip install -r requirements.txt

## Run the application

python -m src.main

# Run all test

python -m pytest

python -m pytest -v

python -m pytest -v tests/test_email_generator_service.py

python -m pytest -v tests/test_api.py

python -m pytest -v tests/test_email_generator_service.py::test_empty_purpose 


