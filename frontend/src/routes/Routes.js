import React from 'react'
import { Route, BrowserRouter, Switch } from 'react-router-dom'
import LandingPage from '../components/containers/LandingPage'
import DashboardPage from '../components/containers/DashboardPage'

const Routes = () => (
    <BrowserRouter>
        <div>
            <Switch>
                <Route exact path='/' component={LandingPage}></Route>
                <Route path='/dashboard' component={DashboardPage}/>
            </Switch>
        </div>
    </BrowserRouter>
)

export default Routes