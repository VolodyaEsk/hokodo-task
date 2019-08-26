import pytest

from app import app


@pytest.fixture(scope='session')
def client():
    client = app.test_client()
    yield client