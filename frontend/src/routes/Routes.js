import React from 'react'
import { Route, BrowserRouter, Switch } from 'react-router-dom'
import LandingPage from '../components/containers/LandingPage'

const Routes = () => (
    <BrowserRouter>
        <div>
            <Switch>
                <Route exact path="/" component={LandingPage}></Route>
            </Switch>
        </div>
    </BrowserRouter>
)

export default Routes