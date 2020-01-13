import { 
    FETCH_ACTORS_REQUEST,
    FETCH_ACTORS_SUCCESS,
    FETCH_ACTORS_FAILURE
} from './actorTypes'

const fetchActorRequest = () => {
    return {
        type: FETCH_ACTORS_REQUEST
    }
}

const fetchActorSuccess = (actors) => {
    return {
        type: FETCH_ACTORS_SUCCESS,
        payload: actors
    }
}

const fetchActorFailure = (error) => {
    return {
        type: FETCH_ACTORS_FAILURE,
        payload: error
    }
}

