import pytest
from src.app import create_app
from flask import Flask 
from flask.testing import FlaskClient

@pytest.fixture
def app() -> Flask: 
    return create_app("tests.settings")

@pytest.fixture()
def client(app) -> FlaskClient:
    return app.test_client()

def test_login(client):

    classification = "teacher"
    for classification in ["teacher", "student"]:
        res = client.post(f"/api/{classification}/login", data={
                "username" : "Mic check",
                "password" : "hunter12",
            })

        json = res.get_json()
        assert res
        assert json["access_token"]

