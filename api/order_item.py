from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json


# ==================================== CONNECTION SPECIFICATION ====================================== #

############ Call Flask, Connect Flask to Database ############
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@127.0.0.1:3306/ecommerce?auth_plugin=mysql_native_password'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

############ Order Item Class Object Creation ############
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
    order_items = Order_Item.query.all()
    return jsonify({"order_items": [order_item.json() for order_item in order_items ]}), 200

    
# =============================== Get item from Order Item by order id and product id================================== #
@app.route("/getOrderItem/<int:order_id>/<int:product_id>", methods=["GET"])
def getOrderItem(order_id, product_id):
    """
    Delete record from order_item
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


if __name__=='__main__':
    app.run(port=5250, debug=True)
