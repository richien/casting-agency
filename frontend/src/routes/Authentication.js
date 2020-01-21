import React from 'react';
import { Redirect } from 'react-router-dom';
import { isAuthenticated } from '../utils/localStorage'


export const Authenticated = Component => props => (
    isAuthenticated ? <Component {...props}/> : <Redirect to="/" />
)

export const UnAuthenticated = Component => props => (
    !isAuthenticated ? <Component {...props}/> : <Redirect to="/dashboard"/>
)