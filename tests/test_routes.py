from tests.conftest import async_client, test_db
import pytest
from sqlalchemy import select
from src.models import Recipe


async def test_main_page(async_client, test_db):
    response = await async_client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'Main page'}

