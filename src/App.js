import Products from "./components/Products";
import "./App.css";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { useState, useEffect } from "react";
import Login from "./components/Login";
import Nav from "./components/Nav";
import Home from "./components/Home";

function App() {
  const [loggedin, setLoggedin] = useState(false);
  const [redirect, setRedirect] = useState(false);

  return (
    <div className="App">
      <Products />
      <Router>
        <Nav loggedin={loggedin} setLoggedin={setLoggedin} setRedirect={setRedirect} />
        <main className="form-signin">
          <Route path="/" exact component={() => <Login loggedin={loggedin} setLoggedin={setLoggedin} redirect={redirect} setRedirect={setRedirect} />} />
          <Route path="/home" component={Home} />
        </main>
      </Router>
    </div>
  );
}

export default App;
