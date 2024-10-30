from tests.conftest import test_client, test_db
from sqlalchemy import select
from src.models import Recipe


def test_main_page(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'Main page'}


def test_database(test_client, test_db):
    stmt = select(Recipe)
    result = test_db.execute(stmt)
    print(result.scalars().all())

