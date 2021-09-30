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
        self.id = id
        self.customer_id = customer_id
        self.status = status
        self.created_at = created_at

    def json(self):
        order_item_entry = {
            "id": self.id,
            "customer_id": self.customer_id,
            "status": self.status,
            "created_at": self.created_at,
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

# =============================== Return List of all products in OrderItem ================================== #
@app.route("/getAllOrderItem", methods=['GET'])
def getAllOrderItem():
    """
    Get all order_items
    """
    order_items = Order_Item.query.all()
    return jsonify({"order_items": [order_item.json() for order_item in order_items ]}), 200

# =============================== Get item from Order Item by order id and product id================================== #
@app.route("/getOrderItem/<int:order_id>/<int:product_id>", methods=["GET"])
def getOrderItem(order_id, product_id):
    """
    Get order_item by order_id and product_id
    """
    order_item = Order_Item.query.filter_by(order_id=order_id, product_id=product_id).first()
    if (order_item):
        return order_item.json(), 200
    return jsonify({"error": f"There is no data with order id: {order_id} and product id: {product_id}"})

# =============================== Delete Items from Order Item ================================== #
@app.route("/deleteOrderItem/<int:order_id>/<int:product_id>", methods=["DELETE"])
def deleteOrderItem(order_id, product_id):
    """
    Delete record from order_item
    """
    order_item = Order_Item.query.filter_by(order_id=order_id, product_id=product_id).first()
    if (order_item):
        db.session.delete(order_item)
        db.session.commit()
        return jsonify({"message" : f"Successfully Deleted order id: {order_id} and product id: {product_id}"})
    return jsonify({"error" : f"There is no data with order id: {order_id} and product id: {product_id}"})

# =============================== Insert Products in Cart into Database ================================== #
@app.route("/addToCart", methods = ['POST'])
def addToCart():


    return jsonify(True)

if __name__=='__main__':
    app.run(port=5000, debug=True)
