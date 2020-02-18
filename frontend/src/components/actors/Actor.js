import React from 'react';
import {Redirect} from 'react-router-dom';
import PropTypes from 'prop-types';

function Actor ({actor, redirect}) {

    const actorUri = `/actors/${actor.id}`,
        renderRedirect = () => {
            if (redirect) {
                return <Redirect to={actorUri} />;
            }
        };
    return (
        <div className="item-wrapper-sm" >
            {renderRedirect()}
            <p>
                {actor.name}
            </p>
        </div>
    );

}

Actor.propTypes = {
    'actor': PropTypes.shape({
        'name': PropTypes.string,
        'id': PropTypes.number
    }),
    'redirect': PropTypes.bool
};

export default Actor;
