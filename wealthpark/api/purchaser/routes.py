import json

from flask import Blueprint, jsonify, request
from sqlalchemy import exc

from wealthpark.api.common.error import MissingParameter, InvalidData
from wealthpark.api.common.error import DatabaseError
from wealthpark.models.purchaser import Purchaser
from wealthpark.database import db

mod = Blueprint('purchaser', __name__)

@mod.route('', methods=['POST'])
def purchaser():
    if request.method == 'POST':
        try:
            data = json.loads(request.data)
            name = data.get('name', None)
            if name == None:
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
        except (ValueError):
            return InvalidData

@mod.route('/<int:purchaser_id>/product', methods=['GET'])
def getPurchaserProducts():
    return ''
