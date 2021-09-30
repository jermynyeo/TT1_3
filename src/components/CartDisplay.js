import React, { useState, useEffect } from "react";

function CartDisplay(props) {
  useEffect(() => {
    // Run! Like go get some data from an API.
    setNum(props.qty);
    console.log(num);
  }, []);
  let [num, setNum] = useState(0);

  const onChangeNum = (e) => {
    console.log(e.target.value);
  };

  return (
    <div className="productDiv">
      <img className="imageSize" src={props.image} alt="Italian Trulli" />
      <div>{props.title}</div>
      <div>${props.price * props.qty} </div>
      <div>
        <input
          type="number"
          class="form-control"
          id="exampleInputEmail1"
          aria-describedby="emailHelp"
          defaultValue={props.qty}
        />
      </div>
      <div className="deleteButton">
        <button
          type="button"
          class="btn btn-danger"
          onClick={() => props.deleteProduct(props.id)}
        >
          delete
        </button>
      </div>
    </div>
  );
}

export default CartDisplay;
