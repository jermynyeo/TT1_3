import React from "react";
import categories from "../data/categories.json";
import products from "../data/products.json";
import "../css/products.css";
import Select from "react-select";
import { useState, useEffect } from "react";
import Button from "./Button";

function Products() {
  async function fetchAllTask() {
    const res = await fetch("http://localhost:5000/getAllproduct");
    const data = await res.json();
    // console.log("Fetched Data:", res.data);
    return data;
  }

  const [products1, setProducts] = useState([]);

  const [tempCart, setCartItems] = useState([]);

  //   useEffect(() => {
  //     async function getProducts() {
  //       const prodFromServer = await fetchAllTask();
  //       setProducts(prodFromServer);
  //     }
  //     getProducts();
  //   }, []);

  const [selId, setCatId] = useState("");
  //   const [selOptions, setSelOptions] = useState([{ value: "All", label: "All" }]);
  function ddlHandler(e) {
    setCatId(e.value);
  }

  function addToCart(item) {
    setCartItems([...tempCart, item]);
  }

  const listItemsSel = products.map((item) =>
    item.category_id === selId ? (
      <div className="card" key={item.id}>
        <div className="card_img">
          <img src={item.image} />
        </div>
        <Button text="Add to Cart" color="green" onClick={(e) => addToCart(item)} />
        <div className="card_header">
          <h2>{item.title}</h2>

          {/* <p className="description">{item.description}</p> */}
          <p className="price">${item.price}</p>
          <p className="qty">Quantity Left: {item.qty}</p>
        </div>
      </div>
    ) : (
      ""
    )
  );

  const listItems = products.map((item) => (
    <div className="card" key={item.id}>
      <div className="card_img">
        <img src={item.image} />
      </div>
      <Button text="Add to Cart" color="green" onClick={(e) => addToCart(item)} />
      {/* <div className="btn" id={item.id} onClick={addToCart(item)}>
        Add to cart
      </div> */}
      <div className="card_header">
        <h2>{item.title}</h2>

        {/* <p className="description">{item.description}</p> */}
        <p className="price">${item.price}</p>
        <p className="qty">Quantity Left: {item.qty}</p>
      </div>
    </div>
  ));

  const options = categories.map((category) => ({ value: category.id, label: category.name }));
  //   setSelOptions([...selOptions, options]);

  return (
    <div className="main_content">
      <div className="product-header">
        <h3>
          <Select options={options} onChange={ddlHandler} />
        </h3>
      </div>
      {selId != "" ? listItemsSel : listItems}
    </div>
  );
}

export default Products;
