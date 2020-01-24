import { 
    FETCH_ACTORS_REQUEST,
    FETCH_ACTORS_SUCCESS,
    FETCH_ACTORS_FAILURE
} from '../actorTypes'
import axios from 'axios'
import config from '../../../auth_config.json'

const endpoint = config.baseApiUrl + '/actors?limit=10'
const token = localStorage.getItem('JWT_TOKEN')
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
        
        dispatch(fetchActorsRequest())
        let headers = {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
        }
        axios.get(endpoint, {'headers': headers})
        .then(response => {
            dispatch(fetchActorsSuccess(response.data))
        })
        .catch(error => {
            dispatch(fetchActorsFailure(error.message))
        })
    }
}

