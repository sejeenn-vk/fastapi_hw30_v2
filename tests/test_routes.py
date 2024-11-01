import pytest
from src.config import Settings
from src.database import async_engine
from src.models import Base


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    print(f"DB_URL={Settings.DB_URL}")
    Base.metadata.drop_all(async_engine)
    Base.metadata.create_all(async_engine)


def test_db(setup_db):
    print(f"DB_URL={Settings.DB_URL}")
