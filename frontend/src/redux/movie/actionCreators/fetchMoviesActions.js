import * as types from '../movieTypes';
import axios from 'axios';
import config from '../../../auth_config.json';

const baseApiUrl = config.baseApiUrl;
const token = localStorage.getItem('JWT_TOKEN');

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
    const token = localStorage.getItem('JWT_TOKEN');
    const headers = {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
    }
    return axios.get(
        baseApiUrl + '/movies?limit=10',
        {'headers': headers})
        .then(res => {
            dispatch(fetchMoviesSuccess(res.data));
        })
        .catch(error => {
            dispatch(fetchMoviesFailure(error.message));
        });
};