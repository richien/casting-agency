import React from 'react';
import { Redirect } from 'react-router-dom';
import PropTypes from 'prop-types';

function Movie({movie, redirect}) {
    const movieUri = `/movies/${movie.id}`;
    const renderRedirect = () => {
        if (redirect) {
            return <Redirect to={movieUri} />;
        }
    };
    return (
        <div className="item-wrapper-sm">
           {renderRedirect()}
           <p>
               {movie.title}
           </p> 
        </div>
    )
}

Movie.propTypes = {
    'movie': PropTypes.shape({
        'title': PropTypes.string,
        'id': PropTypes.number
    }),
    'redirect': PropTypes.bool
}

export default Movie
