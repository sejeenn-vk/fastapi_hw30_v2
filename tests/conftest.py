import pytest
from src.main import app
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.models import Base
from src.database import get_db

from typing import Generator, Any
from asyncio import AbstractEventLoop
from asyncio import get_event_loop_policy
from httpx import AsyncClient, ASGITransport

async_engine_test = create_async_engine(url="sqlite+aiosqlite:///tests/test.db", echo=False)
async_session_test = async_sessionmaker(async_engine_test, expire_on_commit=False)


async def override_get_async_session():
    # Переопределение используемой базы данных
    async with async_session_test() as session:
        yield session

# Переопределение используемой базы данных
app.dependency_overrides[get_db] = override_get_async_session


@pytest.fixture(scope="session", autouse=True)
async def test_db():
    async with async_engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield
    # async with async_engine_test.begin() as conn:
    #     await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
async def async_session():
    async with async_session_test() as session:
        yield session


@pytest.fixture(scope="session", autouse=True)
def event_loop() -> Generator["AbstractEventLoop", Any, None]:
    policy = get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def async_client():
    async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://localhost:8000"
    ) as ac:
        yield ac
