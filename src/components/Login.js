import { Redirect } from "react-router-dom";
import { useState } from "react";
import customers from "../data/customers.json";
import "../css/form.css";


  const Login = ({setLoggedin, redirect, setRedirect, setRegisterRedirect}) => {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    let errorMessage
    setRegisterRedirect(false)

    const onSubmit = async (e) => {
        e.preventDefault()

        const res = await fetch('http://localhost:5000/auth/login' , {
            method: 'POST',
            headers:{'Content-Type': 'application/json'},
            credentials: 'include',         
            body: JSON.stringify({username,password})
        })
        const data = await res.json()
        localStorage.setItem("token", JSON.stringify(data));
        const result = localStorage.getItem('token')
        console.log(result)
        setRedirect(true)
        setLoggedin(true)
        
        // customers.forEach((customer) => {
        //     if (customer.username === username) {
        //         if (customer.password === password) {
        //             setLoggedin(true)
        //             setRedirect(true)
        //         } else {
        //             errorMessage = (<h2>Wrong password</h2>)
        //         }
        //     } else {
        //         errorMessage = (<h2>No account found</h2>)
        //     }
        // })
    }

  if (redirect) {
    return <Redirect to="/home" />;
  } else {
    return (
      <div>
        <form>
          <h1 className="h3 mb-3 fw-normal">Please sign in</h1>

          <div className="form-floating">
            <input
              type="text"
              className="form-control"
              placeholder="Username"
              onChange={(e) => setUsername(e.target.value)}
            />
            <label>Username</label>
          </div>
          <div className="form-floating">
            <input
              type="password"
              className="form-control"
              placeholder="Password"
              onChange={(e) => setPassword(e.target.value)}
            />
            <label>Password</label>
          </div>
          <button
            className="w-100 btn btn-lg btn-primary"
            type="submit"
            onClick={onSubmit}
          >
            Sign in
          </button>
          <div>{errorMessage}</div>
        </form>
      </div>
    );
  }
};

export default Login;
