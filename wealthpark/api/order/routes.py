from flask import Blueprint

mod = Blueprint('purchaser-product', __name__)

@mod.route('', methods=['POST'])
def postOrder():
    return ''
