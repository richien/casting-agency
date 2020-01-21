import React from 'react'
import config from '../../auth_config.json'

let logOutLink = 'https://'
logOutLink += config.domain + '/v2/logout?' + '&'
logOutLink += 'returnTo=' + config.logoutRedirect + '&'
logOutLink += 'client_id=' + config.clientId

function LogoutLink() {
    const logOut = () => {
        localStorage.clear()
        return window.location.replace(logOutLink)
    }
    return (
        <div>
            <button onClick={() => logOut()}>Sign Out</button>
        </div>
    )
}

export default LogoutLink
