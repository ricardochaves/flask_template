import pytest

from app import app


@pytest.fixture
def client():

    client = app.test_client()
    yield client


def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get("/")
    assert b"Hello World!" in rv.data
