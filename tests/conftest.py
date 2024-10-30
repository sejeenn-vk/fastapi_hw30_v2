import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker

from src.main import app
from src.models import Base, Recipe
from src.database import add_data
from tests.data_for_test_db import recipes, ingredients_to_recipes, ingredients

SQLALCHEMY_DATABASE_URL = "sqlite:///tests/test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client


@pytest.fixture(scope="module")
def test_db():
    db = TestingSessionLocal()
    Base.metadata.create_all(bind=engine)
    db.add_all(recipes)
    db.commit()
    # print(stmt)

    yield db
    # Base.metadata.drop_all(bind=engine)
    db.close()

