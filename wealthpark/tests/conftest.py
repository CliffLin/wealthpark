import pytest
from flask import Flask

from wealthpark.config import Testing
from wealthpark.api.product.routes import mod
from wealthpark.database import database, db as _db

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config.from_object(Testing())
    app.test_request_context().push()
    yield app

@pytest.fixture
def client(app):
    database.create_app(app)
    with app.app_context():
        client = app.test_client()
        yield client
        _db.drop_all()
