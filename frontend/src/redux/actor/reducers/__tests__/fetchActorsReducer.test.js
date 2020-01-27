import * as types from '../../actorTypes';
import fetchActorsReducer from '../fetchActorsReducer'

describe('FetchActorsReducer', () => {

    test('should return default state', () => {
        const expectedState = {
            loading: false,
            data: [],
            error: '',
            totalItems: 0
        }

        const newState = fetchActorsReducer(undefined, {});

        expect(newState).toEqual(expectedState)
    });

    test('request action should update loading state', () => {
        const expectedState = {
            loading: true,
            data: [],
            error: '',
            totalItems: 0
        }
        const action = {
            type: types.FETCH_ACTORS_REQUEST
        }

        const newState = fetchActorsReducer(undefined, action);

        expect(newState).toEqual(expectedState)

    });

    test('success action should update data and total items state', () => {
        const expectedState = {
            loading: false,
            data: [{
                name: 'James Doe'
            }],
            error: '',
            totalItems: 1
        }
        const action = {
            type: types.FETCH_ACTORS_SUCCESS,
            payload: {
                actors: [{
                    name: 'James Doe'
                }],
                'total-actors': 1
            }
        }

        const newState = fetchActorsReducer(undefined, action);

        expect(newState).toEqual(expectedState)

    });

    test('success action should not update state without a payload', () => {
        const expectedState = {
            loading: false,
            data: [],
            error: '',
            totalItems: 0
        }
        const action = {
            type: types.FETCH_ACTORS_SUCCESS
        }

        const newState = fetchActorsReducer(undefined, action);

        expect(newState).toEqual(expectedState)

    });

    test('failure action should update error state', () => {
        const expectedState = {
            loading: false,
            data: [],
            error: 'An error occured',
            totalItems: 0
        }
        const action = {
            type: types.FETCH_ACTORS_FAILURE,
            payload: 'An error occured'
        }

        const newState = fetchActorsReducer(undefined, action);

        expect(newState).toEqual(expectedState)

    });

    test('failure action should not update state without a payload', () => {
        const expectedState = {
            loading: false,
            data: [],
            error: '',
            totalItems: 0
        }
        const action = {
            type: types.FETCH_ACTORS_FAILURE
        }

        const newState = fetchActorsReducer(undefined, action);

        expect(newState).toEqual(expectedState)

    });

});