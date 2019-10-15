# pylint: disable=redefined-outer-name

import pytest
from wealthpark.api.order.routes import mod
from wealthpark.models.product import Product
from wealthpark.models.purchaser import Purchaser
from wealthpark.database import db

@pytest.fixture
def app(app):
    app.register_blueprint(mod, url_prefix='/purchaser-product')
    return app

def _postOrder(client, product, purchaser, timestamp):
    return client.post('/purchaser-product', json=dict(
        purchaser_id=purchaser, product_id=product,
        purchase_timestamp=timestamp))

def testPostOrderWithNoneData(client):
    resp = _postOrder(client, 100, 1000, 1566265701)
    assert resp.status_code == 400
    assert resp.json['success'] is False

def testPostorder(client):
    newProduct = Product('testProduct1')
    newPurchaser = Purchaser('testPurchaser1')
    db.session.add(newProduct)
    db.session.add(newPurchaser)
    db.session.commit()

    resp = _postOrder(client, 1, 1, 1566265701)
    assert resp.status_code == 200
    assert resp.json['success'] is True
