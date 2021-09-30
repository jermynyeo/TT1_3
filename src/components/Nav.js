import { Link } from "react-router-dom";
import "../css/navbar.css";

const Nav = ({ loggedin, setLoggedin, setRedirect }) => {
  const onLogout = () => {
    setLoggedin(false);
    setRedirect(false);
  };

  let menu;

  if (loggedin == false) {
    menu = (
      <ul className="container-right">
        <li className="nav-item">
          <Link to="/" className="nav-link active" aria-current="page" href="#">
            Login
          </Link>
        </li>
        <li className="nav-item">
          <Link to="/register" className="nav-link active" aria-current="page" href="#">
            Register
          </Link>
        </li>
      </ul>
    );
  } else {
    menu = (
      <ul className="container-right">
        <li className="nav-item">
          <Link to="/" className="nav-link active" aria-current="page" href="#" onClick={onLogout}>
            Logout
          </Link>
        </li>
      </ul>
    );
  }

  return (
    <div>
      <nav className="navbar navbar-expand-md navbar-dark bg-dark mb-4">
        <div className="container-fluid">
          <Link to="/" className="container-left" href="#">
            Home
          </Link>
          <div className="menu">{menu}</div>
        </div>
      </nav>
    </div>
  );
};

export default Nav;
