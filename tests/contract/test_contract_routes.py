import pytest

from app import app
from jsonschema import FormatChecker
from jsonschema import validate


@pytest.fixture
def client():

    client = app.test_client()
    yield client


def test_contract_githubuser_route(client):
    """Contract: Test githubuser route."""

    schema = {
        "type": "object",
        "properties": {
            "urser_name": {"type": "string"},
            "id": {"type": "integer", "minimum": 1},
            "created_at": {"type": "string", "format": "date-time"},
        },
        "required": ["urser_name", "id", "created_at"],
    }

    response = client.get("/githubuser/ricardochaves")

    validate(response.json, schema, format_checker=FormatChecker())


def test_contract_path_route(client):
    """Contract: Test path route."""

    schema = {"type": "object", "properties": {"your_path": {"type": "string"}}, "required": ["your_path"]}

    response = client.get("/path/hi")

    validate(response.json, schema)
