import React from "react";
import categories from "../data/categories.json";
import products from "../data/products.json";
import "../css/products.css";
import Select from "react-select";

function Products() {
  const listItems = products.map((item) => (
    <div className="card" key={item.id}>
      <div className="card_img">
        <img src={item.image} />
      </div>
      <div className="card_header">
        <h2>{item.title}</h2>

        <p className="description">{item.description}</p>
        <p className="price">${item.price}</p>
        <p className="qty">Quantity Left: {item.qty}</p>
        <div className="btn">Add to cart</div>
      </div>
    </div>
  ));

  const options = categories.map((category) => ({ value: category.id, label: category.name }));

  return (
    <div className="main_content">
      <div className="product-header">
        <h3>
          <Select options={options} />
        </h3>
      </div>
      {listItems}
    </div>
  );
}

export default Products;
