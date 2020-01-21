import React from 'react'
import { Route, Router, Switch } from 'react-router-dom'
import LandingPage from '../components/containers/LandingPage'
import DashboardPage from '../components/containers/DashboardPage'
import history from '../utils/history'
import FooterContainer from '../components/commons/FooterContainer'
import NavBarContainer from '../components/commons/NavBarContainer'
import LoginRedirect from '../components/containers/LoginRedirect'

const Routes = () => (
    <Router history={history}>
        <div>
            <NavBarContainer />
            <Switch>
                <Route exact path='/' component={LandingPage}></Route>
                <Route path='/dashboard' component={DashboardPage}/>
                <Route path='/auth' component={LoginRedirect}/>
            </Switch>
            <FooterContainer />
        </div>
    </Router>
)

export default Routes