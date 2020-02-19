import React from 'react'
import { doLogout } from '../../utils';

function LogoutLink() {
    return (
        <div>
            <button onClick={() => doLogout()}>Sign Out</button>
        </div>
    )
}

export default LogoutLink
