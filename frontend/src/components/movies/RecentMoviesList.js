import React, { useEffect, useState } from 'react';
import { connect } from 'react-redux';
import Spinner from '../commons/Spinner';
import { fetchMovies } from '../../redux/movie';
import Movie from '../movies/Movie';
import formatDate from '../../utils/formatDate';


function RecentMoviesList({fetchMovies, movies, loading}) {
    let [redirect, setRedirect] = useState(false);
    const handleSetRedirect = () => {
        setRedirect(true);
    };
    useEffect(() => {
        fetchMovies();
    }, [fetchMovies]);
    return (
        <div>
            <header><h6>Recently Added Movies</h6></header>
            {
                loading ?
                <div data-test='spinner' className='spinner'><Spinner/></div> :
                movies.map((movie, index, movies) => (
                    <div data-test='list-wrapper' className='list-wrapper' key={movie.id} onClick={() => handleSetRedirect()}>
                        <p>{index + 1}</p>
                        <span>
                            <Movie movie={movie} redirect={redirect} key={movie.id}/>
                        <div className='joined-date-wrapper'><i>Added: {formatDate(movies[index]['created-at'])}</i></div>
                        </span>
                    </div>
                ))
            }
        </div>
    )
}

const mapStateToProps = (state) => ({
    movies: state.movies.data,
    loading: state.movies.loading
});

const mapDispatchToProps = (dispatch) => ({
    fetchMovies: () => dispatch(fetchMovies())
});

export default connect(
        mapStateToProps,
        mapDispatchToProps
    )(RecentMoviesList);
