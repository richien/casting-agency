import * as types from '../movieTypes';

const initialState = {
    loading: false,
    data: [],
    totalItems: 0,
    error: ''
}

const fetchMoviesReducer = (state=initialState, action) => {
    switch(action.type) {
        case types.FETCH_MOVIES_REQUEST:
            return {
                ...state,
                loading:true
            }
        case types.FETCH_MOVIES_SUCCESS:
            if (action.payload && Object.keys(action.payload).length !== 0) {
                return {
                    ...state,
                    loading: false,
                    data: action.payload.movies,
                    totalItems: action.payload['total-movies'],
                    error: ''
                }
            }
            return state;
        case types.FETCH_MOVIES_FAILURE:
            if (action.payload && Object.keys(action.payload).length !== 0) {
                return {
                    ...state,
                    error: action.payload
                }
            }
            return state;
        default: 
            return state;
    }
}

export default fetchMoviesReducer;