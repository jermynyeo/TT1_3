import { useState } from "react"
import { Redirect } from "react-router-dom"
import customers from '../data/customers.json'

const Register = ({setRedirect, redirect}) => {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [firstName, setFirstName] = useState('')
    const [lastName, setLastName] = useState('')
    const [postal, setPostal] = useState('')
    const [gender, setGender] = useState('')
    let id

    const onSubmit = async (e) => {
        e.preventDefault()
        setRedirect(true)
        id = customers.at(-1).id + 1
        
    }

    if (redirect) {
        return <Redirect to="/" />
    } else {
        return (
            <div>
                <form onSubmit={onSubmit}>
                    <h1 className="h3 mb-3 fw-normal">Please register</h1>
                    <div className="form-floating">
                        <input type="text" className="form-control" placeholder="username" onChange={(e) => setUsername(e.target.value)}/>
                        <label>Username</label>
                    </div>
                    <div className="form-floating">
                        <input type="text" className="form-control" placeholder="firstname" onChange={(e) => setFirstName(e.target.value)}/>
                        <label>First Name</label>
                    </div>
                    <div className="form-floating">
                        <input type="text" className="form-control" placeholder="lastname" onChange={(e) => setLastName(e.target.value)}/>
                        <label>Last Name</label>
                    </div>
                    <div className="form-floating">
                        <input type="postal-code" className="form-control" placeholder="username" onChange={(e) => setPostal(e.target.value)}/>
                        <label>Postal Code</label>
                    </div>
                    <div className="form-floating">
                        <input type="text" className="form-control" placeholder="username" onChange={(e) => setGender(e.target.value)}/>
                        <label>Gender</label>
                    </div>
                    <div className="form-floating">
                        <input type="password" className="form-control" placeholder="password" onChange={(e) => setPassword(e.target.value)} />
                        <label>Password</label>
                    </div>

                    <button className="w-100 btn btn-lg btn-primary" type="submit">Register</button>
                </form>
            </div>
        )
    }
}

export default Register
