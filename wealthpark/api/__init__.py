from flask import Flask
from wealthpark.api.purchaser.routes import mod as purchaser_mod
from wealthpark.api.order.routes import mod as order_mod
from wealthpark.api.product.routes import mod as product_mod

app = Flask(__name__)

app.register_blueprint(purchaser_mod, url_prefix='/purchaser')
app.register_blueprint(order_mod, url_prefix='/purchaser-product')
app.register_blueprint(product_mod, url_prefix='/product')
