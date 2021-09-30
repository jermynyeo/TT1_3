import React from "react";
import categories from "../data/categories.json";
import products from "../data/products.json";
import "../css/products.css";
import Select from "react-select";
import { useState, useEffect } from "react";

function Products() {
  const [selId, setCatId] = useState("");
  console.log(selId);

  function ddlHandler(e) {
    setCatId(e.value);
  }

  const listItems = products.map((item) =>
    item.category_id === selId ? (
      <div className="card" key={item.id}>
        <div className="card_img">
          <img src={item.image} alt="img" />
        </div>
        <div className="btn">Add to cart</div>
        <div className="card_header">
          <h2>{item.title}</h2>
          <p className="price">${item.price}</p>
          <p className="qty">Quantity Left: {item.qty}</p>
        </div>
      </div>
    ) : (
      ""
    )
  );

  const options = categories.map((category) => ({
    value: category.id,
    label: category.name,
  }));

  return (
    <div className="main_content">
      <div className="product-header">
        <h3>
          <Select options={options} onChange={ddlHandler} />
        </h3>
      </div>
      {listItems}
    </div>
  );
}

export default Products;
