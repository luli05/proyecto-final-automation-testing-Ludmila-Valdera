import pytest
import requests
from utils.data_loader import load_data

pytestmark = pytest.mark.api
BASE_URL = "https://jsonplaceholder.typicode.com/posts"

@pytest.fixture
def session():
    with requests.Session() as client:
        yield client

def test_get_posts(session):
    response = session.get(BASE_URL, timeout=15)
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list) and posts
    assert all({"id", "userId", "title", "body"} <= post.keys() for post in posts)

def test_get_post(session):
    response = session.get(f"{BASE_URL}/1", timeout=15)
    assert response.status_code == 200
    post = response.json()
    assert post["id"] == 1
    assert isinstance(post["title"], str) and post["title"]
    assert isinstance(post["body"], str)

def test_create_post(session):
    payload = load_data()["post"]
    response = session.post(BASE_URL, json=payload, timeout=15)
    assert response.status_code == 201
    result = response.json()
    assert isinstance(result["id"], int)
    for key, value in payload.items():
        assert result[key] == value

def test_delete_post(session):
    response = session.delete(f"{BASE_URL}/1", timeout=15)
    assert response.status_code == 200
    assert response.json() == {}

def test_get_missing_post(session):
    response = session.get(f"{BASE_URL}/999999", timeout=15)
    assert response.status_code == 404
    assert response.json() == {}
