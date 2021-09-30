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

    def __init__(self, product_id, order_id, product_qty, total_price):
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

    def __init__(self, id, title, price, description, category_id, image, qty):
        self.id = id
        self.title = title
        self.price = price
        self.description = description
        self.category_id = category_id
        self.image = image
        self.qty = qty
        
    def json(self):
        product_entry = {
            "id": self.id,
            "customer_id": self.customer_id,
            "price": self.price,
            "description": self.description,
            "category_id": self.category_id,
            "image": self.image,
            "qty": self.qty,
        }
        return product_entry


######### Order Object Creation #########
class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.Date, nullable=False)

    def __init__(self, customer_id, status, created_at):
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

# =============================== Get User's Cart  ================================== #
@app.route("/getCart", methods = ['GET'])
def getCart():
    # check if user already has an order
    # data = request.get_json()
    # data = json.loads(data)

    # customer_id = data['customer_id']

    customer_id = 2

    order = Order.query.filter_by(customer_id=customer_id).first()

    # assuming that each user will only make 1 order 

    if (not order):
        return jsonify({"order_items" : []}), 200
        
    order_id = order.id
    order_items = getOrderItems(order_id)
    return jsonify({"order_items": order_items}), 200


# =============================== Insert Products in Cart into Database ================================== #
@app.route("/addToCart", methods = ['POST'])
def addToCart():
    # check if user already has an order
    data = request.get_json()

    # data = json.loads(data)

    customer_id = data['customer_id']
    order = Order.query.filter_by(customer_id=customer_id).first()

    # assuming that each user will only make 1 order 

    if (not order):
        order = Order(customer_id, status, created_at)
        
    product_id = data['product_id']
    product_price = getProductPrice(product_id)

    order_id = order.id
    
    # Item Exists
    order_item = getOrderItemByProduct(order_id, product_id)
    
    if order_item != None:
        product_qty = order_item.product_qty + 1
        if ('product_qty' in data.keys()):
            product_qty = data['product_qty']
        total_price = product_price * product_qty
        return jsonify({"status": updateOrderItem(order_id, product_id, product_qty, total_price)})
    else: 
        # new item
        product_qty = 1
        if ('product_qty' in data.keys()):
            product_qty = data['product_qty']
        total_price = product_price * product_qty
        order_item = Order_Item(product_id, order_id, product_qty, total_price)
        return jsonify({"status": addOrderItem(order_item)})
    
# =============================== Delete Products in Cart into Database ================================== #
@app.route("/deleteFromCart", methods = ['DELETE'])
def deleteFromCart():
    
    data = request.get_json()
    
    order_id = data['order_id']
    product_id = data['product_id']

    return deleteOrderItem(order_id, product_id)

# =============================== Return List of all products of an order in OrderItem ================================== #
def getOrderItems(order_id):
    """
    Get all product in an order_id 
    """
    order_items = Order_Item.query.filter_by(order_id=order_id).all()
    if (order_items):
        return [order_item.json() for order_item in order_items ]
    return []

# =============================== Return orderitem by product and order ================================== #
def getOrderItemByProduct(order_id, product_id):
    """
    Get all product in an order_id 
    """
    return Order_Item.query.filter_by(order_id=order_id, product_id=product_id).first()

# =============================== Add Items from Order Item ================================== #
def addOrderItem(order_item):
    """
    Add record to order_item
    """
    db.session.add(order_item)
    db.session.commit()

    if (Order_Item.query.filter_by(order_id=order_item.order_id, product_id=order_item.product_id).first()):
        return "Item Creation Successful"
    return "Item Creation Failed"

# =============================== Add Items from Order Item ================================== #
def updateOrderItem(order_id, product_id, product_qty, total_price):
    """
    Update record to order_item
    """
    if (product_qty <= 0):
        deleteOrderItem(order_id, product_id)
    else:
        order_item = Order_Item.query.filter_by(order_id = order_id, product_id = product_id).first()
        order_item.product_qty = product_qty
        order_item.total_price = total_price
        db.session.commit()
    return "Successful Update"

# =============================== Delete Items from Order Item ================================== #
def deleteOrderItem(order_id, product_id):
    """
    Delete record from order_item
    """
    order_item = Order_Item.query.filter_by(order_id=order_id, product_id=product_id).first()
    if (order_item):
        db.session.delete(order_item)
        db.session.commit()
        return "Successfully Deleted"
    return "Record does not exist"

def getProductPrice(product_id):
    product = Product.query.get(product_id)
    return product.price


if __name__=='__main__':
    app.run(port=5000, debug=True)
