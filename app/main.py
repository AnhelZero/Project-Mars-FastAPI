from fastapi import FastAPI
from .serials import Serial

app = FastAPI(title="FastAPI by JustUta")


@app.get('/')
def home():
    return {'Система':'работает успешно'}


@app.get('/{id}')
def test_project(test: int, q: int = None):
    return {'key': id, 'q': q}

#/"Укажите целое число"?q= "Укажите в виде строки"

@app.get('/id/{id}/name/{name}')
def id_and_name(id: int, name: str):
    return {'id': id, 'name': name}


@app.post('/Serial')
def createserial(item: Serial):
    return item