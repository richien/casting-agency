import React from 'react'
import { Link } from 'react-router-dom'

function SideMenuLinks() {
    return (
        <div>
            <ul>
                <li><Link to='/actors'>Actors</Link></li>
                <li><Link to='/movies'>Movies</Link></li>
            </ul>
        </div>
    )
}

export default SideMenuLinks