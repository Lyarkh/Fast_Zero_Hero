from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero_hero.schemas import Message, UserSchema

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello world'}


@app.get('/hello-world-html', status_code=HTTPStatus.OK)
def read_root_html():
    return HTMLResponse('<h1>Hello world</h1>')


@app.post('/users/', status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):
    return user