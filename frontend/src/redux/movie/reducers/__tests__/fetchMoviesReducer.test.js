import * as types from '../../movieTypes';
import fetchMoviesReducer from '../fetchMoviesReducer';

const initialState = {
    loading: false,
    data: [],
    error: '',
    totalItems: 0
};

describe('fetch movies reducer', () => {
    test('should set state the default state', () => {
        const newState = fetchMoviesReducer(undefined, {});
        expect(newState).toEqual(initialState);
    });
    test('request action should set loading to true', () => {
        const expectedState = {
            ...initialState,
            loading: true,
        }
        const action = {
            type: types.FETCH_MOVIES_REQUEST
        }
        const newState = fetchMoviesReducer(undefined, action);
        expect(newState).toEqual(expectedState); 
    });

    test('success action with payload should update state', () => {
        const data = {
            movies: [{title: 'test movie'}],
            'total-movies': 1
        }
        const expectedState = {
            ...initialState,
            data: data.movies,
            totalItems: data['total-movies']
        }
        const action = {
            type: types.FETCH_MOVIES_SUCCESS,
            payload: data
        }
        const newState = fetchMoviesReducer(undefined, action);
        expect(newState).toEqual(expectedState);
    });

    test('success action without payload should not update state', () => {
        const action = {
            type: types.FETCH_MOVIES_SUCCESS
        }
        const newState = fetchMoviesReducer(undefined, action);
        expect(newState).toEqual(initialState);
    });
    test('success action with an empty payload should not update state', () => {
        const action = {
            type: types.FETCH_MOVIES_SUCCESS,
            payload: {}
        }
        const newState = fetchMoviesReducer(undefined, action);
        expect(newState).toEqual(initialState);
    });

    test('failure action with payload should update state', () => {
        const errorMessage = 'Something went wrong';
        const expectedState = {
            ...initialState,
            error: errorMessage
        };
        const action = {
            type: types.FETCH_MOVIES_FAILURE,
            payload: errorMessage
        }
        const newState = fetchMoviesReducer(undefined, action);
        expect(newState).toEqual(expectedState);
    });

    test('failure action without payload should not update state', () => {
        const action = {
            type: types.FETCH_MOVIES_FAILURE,
        }
        const newState = fetchMoviesReducer(undefined, action);
        expect(newState).toEqual(initialState);
    });

    test('failure action with an empty payload should not update state', () => {
        const action = {
            type: types.FETCH_MOVIES_FAILURE,
            payload: {}
        }
        const newState = fetchMoviesReducer(undefined, action);
        expect(newState).toEqual(initialState);
    });
});