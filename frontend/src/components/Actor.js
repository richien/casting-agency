import React, { useState } from 'react'
import {Redirect} from 'react-router-dom';

function Actor({actor, redirect}) {
    const actorUri = `/actors/${actor.id}`
    const renderRedirect = () => {
        if(redirect) {
            return <Redirect to={actorUri}/>
        }
    }
    return (
        <div className='actor-wrapper-sm' >
            {renderRedirect()}
            <p>{actor.name}</p>
        </div>
    )
}

export default Actor