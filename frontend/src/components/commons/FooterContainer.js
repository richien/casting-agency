import React from 'react'

function FooterContainer() {
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
                    <li><a className="black-text" href="/">Home</a></li>
                    <li><a className="black-text" href="/about">About</a></li>
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

export default FooterContainer
