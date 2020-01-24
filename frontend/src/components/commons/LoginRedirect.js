import React from 'react'
import Spinner from './Spinner'

function LoginRedirect() {

    const storeJwt = () => {
        const fragment = window.location.hash.substr(1).split('&')[0].split('=')
        if (fragment[0] === 'access_token') {
            localStorage.setItem('JWT_TOKEN', fragment[1])
        }
    }

    const setIsAuthenticated = () => {
        const token = localStorage.getItem('JWT_TOKEN')
        if(token) {
            localStorage.setItem('isAuthenticated', true)
        }
    }

    const redirect = () => {
        storeJwt()
        setIsAuthenticated()
        return window.location.replace('/dashboard')
    }

    return (
        <div className="content-wrapper spinner">
            <Spinner/>
            {redirect()}
        </div>
    )
}

export default LoginRedirect
