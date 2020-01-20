import React from 'react'

function DashboardPage() {
    return (
        <div className='content-wrapper'>
            <div className='row start-xs'>
                <div className='col-xs-3'>
                    <div className='box'>
                        <div className='sidebar-menu'></div>
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

export default DashboardPage
