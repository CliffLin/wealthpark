import pytest
from wealthpark.tests.conftest import app
from wealthpark.api.purchaser.routes import mod

@pytest.fixture
def app(app):
    app.register_blueprint(mod, url_prefix='/purchaser')
    return app

def testGetProduct(client):
    resp = client.get('/purchaser')
    assert resp.status_code == 405

def _postProduct(client, name):
    return client.post('/purchaser', json={'name': name})

def testPostProduct(client):
    resp = _postProduct(client, 'bob')
    assert resp.status_code == 200
    assert resp.json['success'] == True

def testPostSameProduct(client):
    resp = _postProduct(client, 'bob')
    assert resp.status_code == 200
    assert resp.json['success'] == True
    resp = _postProduct(client, 'bob')
    assert resp.status_code == 400
    assert resp.json['success'] == False

