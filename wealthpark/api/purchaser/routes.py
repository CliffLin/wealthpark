import json
import datetime

from flask import Blueprint, jsonify, request
from sqlalchemy import exc, func

from wealthpark.api.common.error import MissingParameter, InvalidData
from wealthpark.api.common.error import DatabaseError
from wealthpark.models.purchaser import Purchaser
from wealthpark.models.product import Product
from wealthpark.models.order import Order
from wealthpark.database import db

mod = Blueprint('purchaser', __name__)

@mod.route('', methods=['POST'])
def purchaser():
    try:
        data = json.loads(request.data)
        name = data.get('name', None)
        if name is None:
            return MissingParameter

        newPurchaser = Purchaser(name)
        db.session.add(newPurchaser)
        try:
            db.session.commit()
            db.session.refresh(newPurchaser)
            return jsonify(
                {
                    'success': True,
                    'result': newPurchaser.as_dict()})
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            return DatabaseError(e)
    except ValueError:
        return InvalidData

@mod.route('/<int:purchaser_id>/product', methods=['GET'])
def getPurchaserProducts(purchaser_id):
    start = request.args.get('start_date')
    end = request.args.get('end_date')

    query = db.session.query(
        func.strftime('%Y-%m-%d', Order.purchase_timestamp),
        func.group_concat(Product.name, ';')
    ).join(Product).filter(
        Order.purchaser_id == purchaser_id
    )
    if start:
        start = datetime.datetime.fromisoformat('%sT00:00:00+09:00' % start)
        query = query.filter(Order.purchase_timestamp >= start)
    if end:
        end = datetime.datetime.fromisoformat('%sT00:00:00+09:00' % end) + \
                datetime.timedelta(days=1)
        query = query.filter(Order.purchase_timestamp <= end)
    
    try:
        rows = query.group_by(
            func.strftime('%Y-%m-%d', Order.purchase_timestamp)
        ).all()
        ret = dict()
        for row in rows:
            ret[row[0]] = [dict(product=i) for i in row[1].split(';')]
    
        return jsonify(dict(purchases=ret))

    except exc.SQLAlchemyError as e:
        return DatabaseError(e)
