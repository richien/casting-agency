import React from 'react'
import { Link } from 'react-router-dom'

function Footer() {
    const today = new Date();
    return (
        <footer className="page-footer">
          <div className="container">
            <div className="row">
              <div className="col l6 s12">
                <h5 id="brand-logo-img"></h5>
              </div>
              <div className="col l4 offset-l2 s12">
                <h5 className="black-text">Visit</h5>
                <ul>
                    <li><Link className="black-text" to="/">Home</Link></li>
                    <li><Link className="black-text" to="/about">About</Link></li>
                </ul>
              </div>
            </div>
          </div>
          <div className="footer-copyright">
            <div className="container">
            © {today.getFullYear()}
            </div>
          </div>
        </footer>
    )
}

export default Footer
