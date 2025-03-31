import pytest
from fastapi import status


def test_create_task(client):
    """Test creating a new task."""
    response = client.post(
        "/tasks/", json={"title": "Test Task", "description": "This is a test task"}
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "This is a test task"
    assert "id" in data
    # Strictly check that completed exists and is False
    assert "completed" in data, "completed field is missing from response"
    assert data["completed"] is False


def test_get_tasks(client):
    """Test retrieving all tasks."""
    # Create a task first
    client.post("/tasks/", json={"title": "Test Task", "description": "This is a test task"})

    response = client.get("/tasks/")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_get_task_by_id(client):
    """Test retrieving a task by its ID."""
    # Create a task first
    create_response = client.post(
        "/tasks/", json={"title": "Test Get Task", "description": "Task to be retrieved"}
    )
    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == "Test Get Task"
    assert data["description"] == "Task to be retrieved"


def test_get_nonexistent_task(client):
    """Test attempt to retrieve a nonexistent task."""
    response = client.get("/tasks/9999")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_mark_task_complete(client):
    """Test marking a task as completed."""
    # Create a task first
    create_response = client.post(
        "/tasks/", json={"title": "Task to Complete", "description": "This will be completed"}
    )
    task_id = create_response.json()["id"]

    # Mark the task as completed
    complete_response = client.put(f"/tasks/{task_id}/complete")
    assert complete_response.status_code == status.HTTP_200_OK
    data = complete_response.json()
    # Strictly check that completed exists and is True
    assert "completed" in data, "completed field is missing from response"
    assert data["completed"] is True

    # Verify the task is marked as completed
    get_response = client.get(f"/tasks/{task_id}")
    get_data = get_response.json()
    # Strictly check that completed exists and is True
    assert "completed" in get_data, "completed field is missing in GET response"
    assert get_data["completed"] is True


def test_delete_task(client):
    """Test deleting a task."""
    # Create a task first
    create_response = client.post(
        "/tasks/", json={"title": "Task to Delete", "description": "This will be deleted"}
    )
    task_id = create_response.json()["id"]

    # Delete the task
    delete_response = client.delete(f"/tasks/{task_id}")
    # API returns 204 No Content, not 200 OK
    assert delete_response.status_code == status.HTTP_204_NO_CONTENT

    # Verify the task is deleted
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == status.HTTP_404_NOT_FOUND
