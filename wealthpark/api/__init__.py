from flask import Flask
from wealthpark.api.purchaser.routes import mod
from wealthpark.api.order.routes import mod
from wealthpark.api.product.routes import mod

app = Flask(__name__)

app.register_blueprint(purchaser.routes.mod, url_prefix='/purchaser')
app.register_blueprint(order.routes.mod, url_prefix='/purchaser-product')
app.register_blueprint(product.routes.mod, url_prefix='/product')
