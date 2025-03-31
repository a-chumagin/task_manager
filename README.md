# FastAPI Task Manager

A simple task manager API built with FastAPI, SQLAlchemy, and SQLite. This application allows you to add, delete, and mark tasks as done, as well as retrieve all tasks and tasks by ID.

> **Note:** This repository was created by a GenAi Agent.

## Features

- Create new tasks
- List all tasks
- Get task by ID
- Mark tasks as completed
- Delete tasks
- Uses SQLite for storage
- Docker Compose setup for easy deployment
- Standard pip package manager for Python dependencies

## Development

### Running Tests

To run the unit tests:

```bash
pytest -v
```

### Linting

This project uses flake8, black, and isort for code quality:

```bash
# Run flake8 to check code quality
flake8 .

# Run black to check code formatting
black --check .

# Run isort to check import sorting
isort --check-only .

# Format code with black and isort
black .
isort .
```

### CI/CD

This project includes a GitHub Actions workflow that runs on push to the main branch and on pull requests. The workflow:

1. Installs dependencies
2. Runs linting checks (flake8, black, isort)
3. Runs unit tests with pytest

## Running the application

### Prerequisites

- Docker and Docker Compose

### Starting the application

```bash
docker-compose up -d
```

The API will be available at http://localhost:8000

### API Documentation

Once the application is running, you can access the API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

- `GET /` - Welcome message
- `POST /tasks/` - Create a new task
- `GET /tasks/` - List all tasks
- `GET /tasks/{task_id}` - Get a task by ID
- `PUT /tasks/{task_id}/complete` - Mark a task as completed
- `DELETE /tasks/{task_id}` - Delete a task

## Example Usage

### Create a task

```bash
curl -X 'POST' \
  'http://localhost:8000/tasks/' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread"
}'
```

### List all tasks

```bash
curl -X 'GET' \
  'http://localhost:8000/tasks/' \
  -H 'accept: application/json'
```

### Get task by ID

```bash
curl -X 'GET' \
  'http://localhost:8000/tasks/1' \
  -H 'accept: application/json'
```

### Mark task as completed

```bash
curl -X 'PUT' \
  'http://localhost:8000/tasks/1/complete' \
  -H 'accept: application/json'
```

### Delete a task

```bash
curl -X 'DELETE' \
  'http://localhost:8000/tasks/1' \
  -H 'accept: application/json'
```