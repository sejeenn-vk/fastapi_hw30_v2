from tests.conftest import test_client, test_db


def test_main_page(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'Main page'}


def test_get_all_recipes(test_client, test_db):
    response = test_client.get("/recipes")

    # assert response.status_code == 200
    