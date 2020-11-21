import pytest
# from sqlalchemy.orm import Session
from loguru import logger
from fastapi.testclient import TestClient

# from app.conftest import override_get_db
from dynaconf import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.main import app
from app.endpoints.deps import get_db


def test_signup(t_client) -> None:

    signup_data = {
            "name": "Jonatas Luiz de Oliveira",
            "mail": "contato@jonatasoliveira.com",
            "password": "asdasd",
            "document": "12345678910",
            "phone": "11912345678"
            }
    r = t_client.post("/user/signup", json=signup_data)

    response = r.json()
    assert r.status_code == 201
    assert response == { 
            'name': 'usuario',
            'message': 'adicionado com sucesso'
            }

    
def test_invalid_signup(t_client) -> None:
    signup_data = {
            "name": "Jonatas Luiz de Oliveira",
            "mail": "contato@jonatasoliveira.me",
            "password": "asdasd",
            }
    r = t_client.post("/user/signup", json=signup_data)

    response = r.json()
    assert r.status_code == 422


def test_signup_new(t_client) -> None:

    signup_data = {
            "name": "Jonh Doe",
            "mail": "contato@jonh.com",
            "password": "secret",
            "document": "12345678911",
            "phone": "11912345678"
            }
    r = t_client.post("/user/signup", json=signup_data)

    response = r.json()
    assert r.status_code == 201
    assert response == { 
            'name': 'usuario',
            'message': 'adicionado com sucesso'
            }


def test_request_token(t_client):
    data = {
          "username": "12345678911",
          "password": "secret",
          }
    r = t_client.post(
            "/user/token",
            data)
    response = r.json()

    assert response.get('token_type') == 'bearer'
    assert r.status_code == 200
