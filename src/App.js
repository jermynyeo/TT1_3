import './App.css';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { useState, useEffect } from 'react';
import Login from './components/Login';
import Nav from './components/Nav';
import Home from './components/Home'
import Register from './components/Register';

function App() {
  const [loggedin, setLoggedin] = useState(false)
  const [loginRedirect, setLoginRedirect] = useState(false)
  const [registerRedirect, setRegisterRedirect] = useState(false)

  return (
    <div className="App">
      <Router>
        <Nav loggedin={loggedin} setLoggedin={setLoggedin} setRedirect={setLoginRedirect}/>
        <main className="form-signin">
          <Route path="/" exact component={() => <Login loggedin={loggedin} setLoggedin={setLoggedin} redirect={loginRedirect} setRedirect={setLoginRedirect} setRegisterRedirect={setRegisterRedirect} />} />
          <Route path="/home" component={Home} />
          <Route path="/register" component={() => <Register redirect={registerRedirect} setRedirect={setRegisterRedirect} />} />
        </main>
      </Router>
    </div>
  );
}

export default App;
