import json

from flask import Blueprint, request, jsonify
from sqlalchemy import exc

from wealthpark.api.common.error import MissingParameter, InvalidData
from wealthpark.api.common.error import DatabaseError
from wealthpark.models.order import Order
from wealthpark.database import db



mod = Blueprint('purchaser-product', __name__)

@mod.route('', methods=['POST'])
def postOrder():
    try:
        data = json.loads(request.data)
        purchaser_id = data.get('purchaser_id', None)
        product_id = data.get('product_id', None)
        purchase_timestamp = data.get('purchase_timestamp', None)

        if not (purchase_timestamp and product_id and purchaser_id):
            return MissingParameter

        newOrder = Order(purchaser_id, product_id, purchase_timestamp)
        db.session.add(newOrder)

        try:
            db.session.commit()
            db.session.refresh(newOrder)
            return jsonify(
                {
                    'success': True,
                    'result': newOrder.as_dict()})
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            return DatabaseError(e)

    except ValueError:
        return InvalidData
