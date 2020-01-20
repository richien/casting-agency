import React from 'react'
import { useAuth0 } from '../containers/ReactAuth0Spa'

function NavBarContainer() {

    const { isAuthenticated, loginWithRedirect, logout } = useAuth0()
    let home;
    let signIn;
    let about;
    let dashboard;
    let signOut;
    if(!isAuthenticated) {
        home = <li><a href="/">Home</a></li>
        signIn = <li><button onClick={() => loginWithRedirect({})}>Sign In</button></li>
        about = <li><a href="/about">About</a></li>
    } else {
        dashboard = <li><a href="/dashboard">Dashboard</a></li>
        signOut = <li><button onClick={() => logout()}>Sign Out</button></li>
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
