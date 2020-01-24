import React from 'react'
import { Route, Router, Switch } from 'react-router-dom'
import Landing from '../components/landing/Landing'
import Dashboard from '../components/dashboard/Dashboard'
import history from '../utils/history'
import Footer from '../components/footer/Footer'
import NavBar from '../components/header/NavBar'
import LoginRedirect from '../components/commons/LoginRedirect'

const Routes = () => (
    <Router history={history}>
        <div>
            <NavBar />
            <Switch>
                <Route exact path='/' component={Landing}></Route>
                <Route path='/dashboard' component={Dashboard}/>
                <Route path='/auth' component={LoginRedirect}/>
            </Switch>
            <Footer />
        </div>
    </Router>
)

export default Routes