import pytest

from app import app


@pytest.fixture
def client():

    client = app.test_client()
    yield client


def test_integration_path_route(client):
    """Integration: Test path route."""

    expected = {"your_path": "hi/my/path"}

    response = client.get("/path/hi/my/path")

    assert response.json == expected
