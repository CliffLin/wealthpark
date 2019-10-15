# pylint: disable=redefined-outer-name

import pytest
from wealthpark.api.product.routes import mod

@pytest.fixture
def app(app):
    app.register_blueprint(mod, url_prefix='/product')
    return app


def testGetProduct(client):
    resp = client.get('/product')
    assert resp.status_code == 405

def _postProduct(client, name):
    return client.post('/product', json={'name': name})

def testPostProduct(client):
    resp = _postProduct(client, 'tomato')
    assert resp.status_code == 200
    assert resp.json['success'] is True

def testPostSameProduct(client):
    resp = _postProduct(client, 'tomato')
    assert resp.status_code == 200
    assert resp.json['success'] is True
    resp = _postProduct(client, 'tomato')
    assert resp.status_code == 400
    assert resp.json['success'] is False
