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


######### Category Object Creation #########
class Category(db.Model):
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
def getcategoryproduct(category_id):
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
@app.route("/ProcessOrder/<int:product_id>", methods = ['POST'])
def ProcessOrder(product_id):
    """
    Updating of product qty
    """
    product = Product.query.filter_by(product_id = product_id)
    
    if (product):
        product.qty = product 
        db.session.commit()

if __name__=='__main__':
    app.run(port=5000, debug=True)