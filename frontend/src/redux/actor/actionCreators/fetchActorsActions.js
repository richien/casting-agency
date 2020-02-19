import { 
    FETCH_ACTORS_REQUEST,
    FETCH_ACTORS_SUCCESS,
    FETCH_ACTORS_FAILURE
} from '../actorTypes';
// import axios from 'axios';
// import config from '../../../auth_config.json';
import { getActors } from '../../../api/actors';

// const endpoint = config.baseApiUrl + '/actors?limit=10';
// const token = localStorage.getItem('JWT_TOKEN');
export const fetchActorsRequest = () => {
    return {
        type: FETCH_ACTORS_REQUEST
    }
}

export const fetchActorsSuccess = (actors) => {
    return {
        type: FETCH_ACTORS_SUCCESS,
        payload: actors
    }
}

export const fetchActorsFailure = (error) => {
    return {
        type: FETCH_ACTORS_FAILURE,
        payload: error
    }
}

export const fetchActors = () => {
    return (dispatch) => {
        dispatch(fetchActorsRequest());
        return getActors()
        .then(data => {
            dispatch(fetchActorsSuccess(data))
        })
        .catch(error => {
            dispatch(fetchActorsFailure(error.response.data))
        });
    }
}

