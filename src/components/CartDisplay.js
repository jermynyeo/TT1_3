function cartDisplay(props) {
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
          value={props.qty}
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

export default cartDisplay;
