from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fast_zero_hero.app import app


@pytest.fixture()
def client():# -> Callable[[], ...]:
    return TestClient(app)

def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello world'}


def test_read_root_html_deve_retornar_ok_e_ola_mundo_com_html_h1(client):
    response = client.get('/hello-world-html')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Hello world</h1>' in response.text


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testeClient',
            'password': 'password',
            'email': 'test@testeclient.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testeClient',
        'email': 'test@testeclient.com',
        'id': 1,
    }
