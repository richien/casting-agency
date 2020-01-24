import { 
    FETCH_ACTORS_REQUEST,
    FETCH_ACTORS_SUCCESS,
    FETCH_ACTORS_FAILURE
} from '../actorTypes'

const initialState = {
    loading: false,
    data: [],
    error: '',
    totalItems: 0
}

const fetchActorsReducer = (state=initialState, action) => {
    switch (action.type) {
        case FETCH_ACTORS_REQUEST:
            return {
                ...state,
                loading: true,
                data: [],
                error: '',
                totalItems: 0
            }
        case FETCH_ACTORS_SUCCESS:
            if(action.payload) {
                return {
                    ...state,
                    loading: false,
                    data: action.payload.actors,
                    error: '',
                    totalItems: action.payload['total-actors']
                }
            }
            return state
        case FETCH_ACTORS_FAILURE:
            if(action.payload) {
                return {
                    ...state,
                    loading: false,
                    data: [],
                    error: action.payload,
                    totalItems: 0
                }
            }
            return state
        default:
            return state
    }
}

export default fetchActorsReducer