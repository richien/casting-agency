import React, { useEffect, useState } from 'react'
import config from '../../auth_config.json'

function LoginLink() {
    const buildLoginLink = () => {
        let link = 'https://'
        link += config.domain
        link += '/authorize?'
        link += 'audience=' + config.audience + '&'
        link += 'response_type=token&'
        link += 'client_id=' + config.clientId + '&'
        link += 'redirect_uri=' + config.loginRedirect
        return link
    }
    const [loginLink, setLoginLink] = useState()
    useEffect(() => {
        const link = buildLoginLink()
        setLoginLink(link)
    }, [])
    const showLoginPage = (link) => {
        window.location.replace(link)
    }
    return (
        <div>
            <button onClick={() => {showLoginPage(loginLink)}}>Sign In</button>
        </div>
    )

}

export default LoginLink
