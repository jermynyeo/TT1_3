import Button from "react-bootstrap/Button";
import Navbar from "./Navbar";
import CartDisplay from "./CartDisplay";
import products from "../data/cart.json";
import React, { useState, useEffect } from "react";

function Cart() {
  let [productData, setProductData] = useState([]);
  useEffect(() => {
    // Run! Like go get some data from an API.
    setProductData(products);
    console.log(productData);
  }, []);

  const deleteProduct = (id) => {
    let newData = productData.filter((x) => x.id !== id);
    setProductData(newData);
  };

  const calculateTotal = () => {
    let total = productData.reduce(
      (prev, curr) => prev + curr.qty * curr.price,
      0
    );
    return total.toFixed(2);
  };

  return (
    <div className="Cart">
      <Navbar />
      <div className="cartDiv">
        <div className="cartProductDiv">
          <div className="shoppingCartGreetings">View your shopping Cart!</div>
          <div className="shoppingCartDisplay">
            {productData.map((curr) => (
              <CartDisplay
                title={curr.title}
                price={curr.price}
                image={curr.image}
                qty={curr.qty}
                id={curr.id}
                deleteProduct={deleteProduct}
              />
            ))}
          </div>
        </div>
        <div className="checkoutWrapper">
          <div className="checkoutGreetings">Checkout here!</div>
          <div className="checkoutDisplay">
            <div className="totalPrice">Total: ${calculateTotal()}</div>
            <div>
              <button type="button" class="btn btn-primary">
                Checkout
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Cart;
