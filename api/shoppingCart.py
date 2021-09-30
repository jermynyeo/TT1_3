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

# =============================== Insert Products in Cart into Database ================================== #
@app.route("/addToCart", methods = ['POST'])
def addToCart():


    return jsonify(True)



if __name__=='__main__':
    app.run(port=5000, debug=True)
