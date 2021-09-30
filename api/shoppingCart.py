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

# ===================================== CLASS / DB SPECIFICATION ====================================== #

######### Booking Class Object Creation #########
class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.Date, nullable=True)

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

############ Booking Product Class Object Creation ############
class Order_Item(db.Model):
    __tablename__ = 'order_item'

    product_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, nullable=False)
    product_qty = db.Column(db.Integer, nullable=True)
    total_price = db.Column(db.Float(precision=2), nullable=True)

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
@app.route("/viewAllOrderItems", methods=['GET'])
def viewAllOrderItems():
    order_items = Order_Item.query.all()
    return jsonify({"order_items": [order_item.json() for order_item in order_items ]}), 200

if __name__=='__main__':
    app.run(port=5250, debug=True)
