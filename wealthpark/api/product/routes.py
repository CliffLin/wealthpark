import json

from flask import Blueprint, request, jsonify
from sqlalchemy import exc

from wealthpark.api.common.error import MissingParameter, InvalidData
from wealthpark.api.common.error import DatabaseError
from wealthpark.models.product import Product
from wealthpark.database import db


mod = Blueprint('product', __name__)

@mod.route('', methods=['POST'])
def postProduct():
    try:
        data = json.loads(request.data)
        name = data.get('name', None)
        if name is None:
            return MissingParameter

        newProduct = Product(name)
        db.session.add(newProduct)

        try:
            db.session.commit()
            db.session.refresh(newProduct)
            return jsonify(
                {
                    'success': True,
                    'result': newProduct.as_dict()})
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            return DatabaseError(e)

    except ValueError:
        return InvalidData
