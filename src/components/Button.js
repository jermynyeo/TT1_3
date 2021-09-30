//creating a reusable button component

import React from "react";
import PropTypes from "prop-types";

//must always pass in props, since button is a component, it will not always have the same
//action when clicking
const Button = ({ text, color, onClick }) => {
  return (
    //pass onClick as a prop for different actions
    <button className="btn" style={{ backgroundColor: color }} onClick={onClick}>
      {text}
    </button>
  );
};

Button.defaultProps = {
  color: "green",
};

Button.propTypes = {
  text: PropTypes.string,
  color: PropTypes.string,
  //set an event
  onClick: PropTypes.func.isRequired,
};

export default Button;
