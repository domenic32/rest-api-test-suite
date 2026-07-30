import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users_status_code_and_headers():
    """Verify that fetching users returns a 200 OK and application/json content type."""
    response = requests.get(f"{BASE_URL}/users")
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "application/json" in response.headers["Content-Type"], "Response is not JSON"

def test_get_single_user_schema():
    """Verify specific user payload structure and field types."""
    user_id = 1
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    
    assert response.status_code == 200
    data = response.json()
    
    # Assert expected keys exist
    assert "id" in data
    assert "name" in data
    assert "email" in data
    
    # Assert field values and types
    assert data["id"] == user_id
    assert isinstance(data["name"], str)
    assert "@" in data["email"]

def test_create_user_post_request():
    """Verify POST request payload creation and response validation."""
    new_user = {
        "name": "Alex Taylor",
        "username": "ataylor",
        "email": "alex.taylor@example.com"
    }
    
    response = requests.post(f"{BASE_URL}/users", json=new_user)
    
    assert response.status_code == 201, f"Expected 201 Created, got {response.status_code}"
    data = response.json()
    
    assert data["name"] == new_user["name"]
    assert "id" in data  # Ensure an ID was assigned to the new resource
