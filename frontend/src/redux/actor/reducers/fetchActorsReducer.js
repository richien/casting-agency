import { 
    FETCH_ACTORS_REQUEST,
    FETCH_ACTORS_SUCCESS,
    FETCH_ACTORS_FAILURE
} from '../actorTypes'

const initialState = {
    loading: false,
    actors: [],
    error: ''
}

const fetchActorsReducer = (state=initialState, action) => {
    switch (action.type) {
        case FETCH_ACTORS_REQUEST:
            return {
                ...state,
                loading: true,
                actors: [],
                error: ''
            }
        case FETCH_ACTORS_SUCCESS:
            if(action.payload) {
                return {
                    ...state,
                    loading: false,
                    actors: action.payload,
                    error: ''
                }
            }
            return state
        case FETCH_ACTORS_FAILURE:
            if(action.payload) {
                return {
                    ...state,
                    loading: false,
                    actors: [],
                    error: action.payload
                }
            }
            return state
        default:
            return state
    }
}

export default fetchActorsReducer