import React from 'react'
import { UnAuthenticated } from '../../routes/Authentication'

function LandingPage() {
    return (
        <>
            <div id="bg-image-wrapper">
                <div className="row start-xs" id="text-left">
                    <p>cast in the right movie</p>
                </div>
                <div className="row end-xs" id="text-right">
                    <p>cast at the right time</p>
                </div>
            </div>
        </>
        
    )
}

export default UnAuthenticated(LandingPage)
