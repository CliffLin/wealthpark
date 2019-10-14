from flask import Blueprint

mod = Blueprint('purchaser', __name__)

@mod.route('', methods=['POST'])
def purchaser():
    return ''

@mod.route('/<int:purchaser_id>/product', methods=['GET'])
def getPurchaserProducts():
    return ''
