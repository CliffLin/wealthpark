from flask import Blueprint

mod = Blueprint('product', __name__)

@mod.route('', methods=['POST'])
def postProduct():
    return ''
