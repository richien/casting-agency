import React, {useState, useEffect} from 'react'
import Profile from '../user/Profile'
import SideMenuLinks from '../commons/SideMenuLinks'
import RecentActorsList from '../actors/RecentActorsList'
// import {connect} from 'react-redux'
import { Authenticated } from '../../routes/Authentication'

function Dashboard({fetchActors, actorsList}) {

    return (
        <div className='content-wrapper'>
            <div className='row start-xs'>
                <div className='col-xs-3'>
                    <div className='box'>
                        <div className='sidebar-menu'>
                            <div>
                                {/* <Profile user={user} /> */}
                                <SideMenuLinks />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div className='row end-xs'>
                <div className='col-xs-9'>
                    <div className='main-content'>
                        <div className='row'>
                            <div className='row start-xs'>
                                <div className='col-xs-4'>
                                    <div className='box'>
                                        <div className='content-box'>
                                            <RecentActorsList />
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div className='row end-xs'>
                                <div className='col-xs-4'>
                                    <div className='box'>
                                        <div className='content-box'></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className='row'>
                            <div className='row start-xs'>
                                <div className='col-xs-4'>
                                    <div className='box'>
                                        <div className='content-box'></div>
                                    </div>
                                </div>
                            </div>
                            <div className='row end-xs'>
                                <div className='col-xs-4'>
                                    <div className='box'>
                                        <div className='content-box'></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

// const mapStateToProps = (state) => ({
//     actorsList: state.actor.actors    
// })

// const mapDispatchToProps = (dispatch) => {
//     return {
//         fetchActors: () => dispatch(fetchActors())
//     }
// }
export default Authenticated(Dashboard)
