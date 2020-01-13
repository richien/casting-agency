import React from 'react'

function NavBarContainer() {
    return (
            <nav className="nav-theme">
                <div className="nav-wrapper">
                    <div className="brand-logo" id="brand-logo-img">
                    </div>
                    <ul id="nav-mobile" className="right hide-on-med-and-down">
                        <li><a href="/">Home</a></li>
                        <li><a href="/signin">Sign In</a></li>
                        <li><a href="/about">About</a></li>
                    </ul>
                </div>
            </nav>
    )
}

export default NavBarContainer
