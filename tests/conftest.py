import pytest
from fastapi.testclient import TestClient
from src.database import async_session
from src.main import app


@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client


@pytest.fixture(scope="module")
def test_db():
    db = async_session()
    yield db
    db.close()

