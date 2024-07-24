from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero_hero.app import app

client = TestClient(app)


def test_read_root_deve_retornar_ok_e_ola_mundo():
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello world'}


def test_read_root_html_deve_retornar_ok_e_ola_mundo_com_html_h1():
    response = client.get('/hello-world-html')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Hello world</h1>' in response.text
