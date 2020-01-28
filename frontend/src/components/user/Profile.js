import React from 'react'

function Profile({user}) {
    return (
        <div className="row">
            <div className="col s12 m12">
                <div className="card">
                    <div className="card-image">
                        <img src={user.picture} alt='profile' />
                    </div>
                    <div className="card-content">
                        <p data-test="username">{user.name}</p>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Profile