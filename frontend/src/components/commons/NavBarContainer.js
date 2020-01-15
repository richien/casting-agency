import React from 'react'
import { useAuth0 } from '../containers/ReactAuth0Spa'

function NavBarContainer() {

    const { isAuthenticated, loginWithRedirect, logout } = useAuth0()

    return (
            <nav className="nav-theme">
                <div className="nav-wrapper">
                    <div className="brand-logo" id="brand-logo-img">
                    </div>
                    <ul id="nav-mobile" className="right hide-on-med-and-down">
                        <li><a href="/">Home</a></li>
                        <li>{!isAuthenticated && (
                            <button onClick={() => loginWithRedirect({})}>Sign In</button>
                        )}
                        {isAuthenticated && <button onClick={() => logout()}>Sign Out</button>}
                        </li>
                        <li><a href="/about">About</a></li>
                    </ul>
                </div>
            </nav>
    )
}

export default NavBarContainer
