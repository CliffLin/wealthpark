# pylint: disable=redefined-outer-name

import time
import datetime
import pytest

from wealthpark.api.purchaser.routes import mod
from wealthpark.database import db
from wealthpark.models.product import Product
from wealthpark.models.purchaser import Purchaser
from wealthpark.models.order import Order


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
    assert resp.json['success'] is True

def testPostSameProduct(client):
    resp = _postProduct(client, 'bob')
    assert resp.status_code == 200
    assert resp.json['success'] is True
    resp = _postProduct(client, 'bob')
    assert resp.status_code == 400
    assert resp.json['success'] is False

def testQueryPurchase(client):
    newProduct1 = Product('testProduct1')
    db.session.add(newProduct1)

    newProduct2 = Product('testProduct2')
    db.session.add(newProduct2)

    newProduct3 = Product('testProduct3')
    db.session.add(newProduct3)

    newPurchaser = Purchaser('testPurchaser1')
    db.session.add(newPurchaser)

    db.session.commit()
    db.session.refresh(newProduct1)
    db.session.refresh(newProduct2)
    db.session.refresh(newProduct3)
    db.session.refresh(newPurchaser)
    newOrder = Order(
        newPurchaser.id, newProduct1.id,
        int(time.mktime(
            datetime.datetime(2019, 8, 1).timetuple())+60*60*9))
    db.session.add(newOrder)
    db.session.commit()

    newOrder = Order(
        newPurchaser.id, newProduct2.id,
        int(time.mktime(
            datetime.datetime(2019, 8, 1).timetuple())+60*60*9))
    db.session.add(newOrder)
    db.session.commit()

    newOrder = Order(
        newPurchaser.id, newProduct3.id,
        int(time.mktime(
            datetime.datetime(2019, 8, 5).timetuple())+60*60*9))
    db.session.add(newOrder)

    db.session.commit()

    resp = client.get(
        '/purchaser/%s/product' % newPurchaser.id +
        '?start_date=2019-08-01&end_date=2019-08-05')

    assert len(resp.json['purchases'].keys()) == 2
    assert len(resp.json['purchases']['2019-08-01']) == 2
    assert len(resp.json['purchases']['2019-08-05']) == 1

    resp = client.get(
        '/purchaser/%s/product' % newPurchaser.id +
        '?start_date=2019-08-02&end_date=2019-08-05')

    assert len(resp.json['purchases'].keys()) == 1
    assert len(resp.json['purchases']['2019-08-05']) == 1
