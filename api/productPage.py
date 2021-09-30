from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

# ==================================== CONNECTION SPECIFICATION ====================================== #

############ Call Flask, Connect Flask to Database ############
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@127.0.0.1:3306/ecommerce?auth_plugin=mysql_native_password'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

############ Attach Flask app to database / Enable Cross Origin Resource Sharing with Flask app ############
db = SQLAlchemy(app)

class Order_Item(db.Model):
    __tablename__ = 'order_item'

    product_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, primary_key=True, nullable=False)
    product_qty = db.Column(db.Integer, nullable=True)
    total_price = db.Column(db.Float(precision=2), nullable=True)

    def __init__(self, id, customer_id, status, created_at):
        self.product_id = product_id
        self.order_id = order_id
        self.product_qty = product_qty
        self.total_price = total_price

    def json(self):
        order_item_entry = {
            "product_id": self.product_id,
            "order_id": self.order_id,
            "product_qty": self.product_qty,
            "total_price": self.total_price,
        }
        return order_item_entry


######### Product Object Creation #########
class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    image = db.Column(db.Text, nullable=False)
    qty = db.Column(db.Integer, nullable=False)

    def __init__(self, id, customer_id, status, created_at):
        self.id = id
        self.customer_id = customer_id
        self.status = status
        self.created_at = created_at

    def json(self):
        product_entry = {
            "id": self.id,
            "customer_id": self.customer_id,
            "status": self.status,
            "created_at": self.created_at,
        }
        return product_entry


######### Order Object Creation #########
class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.Date, nullable=False)

    def __init__(self, id, customer_id, status, created_at):
        self.id = id
        self.customer_id = customer_id
        self.status = status
        self.created_at = created_at

    def json(self):
        order_entry = {
            "id": self.id,
            "customer_id": self.customer_id,
            "status": self.status,
            "created_at": self.created_at,
        }
        return order_entry

######### Category Object Creation #########
class Order(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)

    def __init__(self, id, name, description, image):
        self.id = id
        self.name = name
        self.description = description
        self.image = image

    def json(self):
        category_entry = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "image": self.image,
        }
        return category_entry


# =============================== Return List of all products ================================== #
@app.route("/getAllproduct", methods=['GET'])
def getAllproduct():
    """
    Get all product
    """
    products = Product.query.all()
    return jsonify({"products": [Product.json() for Product in products]}), 200

# =============================== Return List of category products ================================== # 
@app.route("/getAllproduct/<int:category_id>", methods=['GET'])
def getElectronicsproduct(category_id):
    """
    Get category product
    """
    products = Product.query.filter_by(category_id = category_id).all()
    if len(products) > 0:
        return jsonify({"products": [Product.json() for Product in products]}), 200
    else:
        category = Category.query.filter_by(id = category_id)
        return jsonify({"message" : f"No product under {category}"})

# =============================== Update product quantity ================================== # 
@app.route("/addToCart", methods = ['POST'])
def addToCart():


if __name__=='__main__':
    app.run(port=5000, debug=True)