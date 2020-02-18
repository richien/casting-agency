import * as types from '../movieTypes';
import { getRecentMovies } from '../../../api/movies';

export const fetchMoviesRequest = () => ({
    type: types.FETCH_MOVIES_REQUEST
});

export const fetchMoviesSuccess = data => ({
    type: types.FETCH_MOVIES_SUCCESS,
    payload: data
});

export const fetchMoviesFailure = errormessage => ({
    type: types.FETCH_MOVIES_FAILURE,
    payload: errormessage
});

export const fetchMovies = () => dispatch => {
    dispatch(fetchMoviesRequest());
    return getRecentMovies()
        .then(data => {
            dispatch(fetchMoviesSuccess(data));
        })
        .catch(error => {
            dispatch(fetchMoviesFailure(error.message));
        });
};