import pytest
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


@pytest.fixture
async def client_app():
    return client
