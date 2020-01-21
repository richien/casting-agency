import React from 'react'
import { Link } from 'react-router-dom'
import LoginLink from '../commons/LoginLink'
import LogoutLink from '../commons/LogoutLink'
import { isAuthenticated } from '../../utils/localStorage'

function NavBarContainer() {
    let home;
    let signIn;
    let about;
    let dashboard;
    let signOut;

    if(!isAuthenticated) {
        home = <li><Link to="/">Home</Link></li>
        signIn = <li><LoginLink/></li>
        about = <li><Link to="/about">About</Link></li>
    } else {
        dashboard = <li><Link to="/dashboard">Dashboard</Link></li>
        signOut = <li><LogoutLink/></li>
    }

    return (
            <nav className="nav-theme">
                <div className="nav-wrapper">
                    <div className="brand-logo" id="brand-logo-img">
                    </div>
                    <ul id="nav-mobile" className="right hide-on-med-and-down">
                        {home}
                        {signIn}
                        {about}
                        {dashboard}
                        {signOut}
                    </ul>
                </div>
            </nav>
    )
}

export default NavBarContainer
