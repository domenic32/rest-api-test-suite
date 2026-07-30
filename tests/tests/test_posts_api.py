import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts_limit_and_structure():
    """Verify posts endpoint returns expected quantity and schema."""
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) == 100

def test_get_nonexistent_post_returns_404():
    """Negative testing: Ensure requesting a non-existent ID returns 404."""
    invalid_post_id = 999999
    response = requests.get(f"{BASE_URL}/posts/{invalid_post_id}")
    
    assert response.status_code == 404
