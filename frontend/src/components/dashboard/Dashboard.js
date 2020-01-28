import React from 'react';
import SideMenuLinks from '../commons/SideMenuLinks';
import RecentActorsList from '../actors/RecentActorsList';
import { Authenticated } from '../../routes/Authentication';

function Dashboard() {

    return (
        <div className='content-wrapper'>
            <div className='row start-xs'>
                <div className='col-xs-3'>
                    <div className='box'>
                        <div className='sidebar-menu'>
                            <div>
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

export default Authenticated(Dashboard)
