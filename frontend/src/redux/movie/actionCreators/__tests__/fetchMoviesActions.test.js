import moxios from 'moxios';
import * as actions from '../../../movie';
import * as types from '../../movieTypes';
import { testStore, mockStore } from '../../../../utils';

describe('fetch movie action creators', () => {
    describe('synchronous action creators', () => {
        test('should return a fetch movie request action', () => {
            const expected = {
                type: types.FETCH_MOVIES_REQUEST
            }
            const actual = actions.fetchMoviesRequest();
            expect(actual).toEqual(expected);
        });
    
        test('should return a fetch movie success action', () => {
            const data = {
                movies: [],
                'total-movies': 0
            }
            const expected = {
                type: types.FETCH_MOVIES_SUCCESS,
                payload: data
            }
            const actual = actions.fetchMoviesSuccess(data);
            expect(actual).toEqual(expected);
        });
    
        test('should return a fetch movie failure action', () => {
            const errorMessage = 'Something went wrong';
            const expected = {
                type: types.FETCH_MOVIES_FAILURE,
                payload: errorMessage
            }
            const actual = actions.fetchMoviesFailure(errorMessage);
            expect(actual).toEqual(expected);
        });
    });

    describe('asynchronous action creators', () => {
        beforeEach(() => {
            moxios.install();
        });

        afterEach(() => {
            moxios.uninstall();    
        });
        test('store is updated correctly on a successfull request', async () => {
            const data = {
                movies: [
                    {title: 'Test movie 1'},
                    {title: 'Test movie 2'}
                ],
                'total-movies': 2
            };
            const store = testStore({});
            moxios.wait(() => {
                const request = moxios.requests.mostRecent();
                request.respondWith({
                    status: 200,
                    response: data
                });
            });
            const expectedState = {
                loading: false,
                data: data.movies,
                totalItems: data['total-movies'],
                error: ''
            }

            await store.dispatch(actions.fetchMovies())
            .then(() => {
                const newState = store.getState()['movies'];
                expect(newState).toEqual(expectedState);
            })
        });

        test('store is updated correctly on a failed request', async () => {
            const errorMessage = 'bad request';
            const store = testStore({});
            moxios.wait(() => {
                const request = moxios.requests.mostRecent();
                request.respondWith({
                    status: 400,
                    response: errorMessage
                });
            });
            const expectedState = {
                loading: false,
                data: [],
                totalItems: 0,
                error: errorMessage
            };

            await store.dispatch(actions.fetchMovies())
            .catch(error => {
                const newState = store.getState()['movies'];
                expect(newState).toEqual(expectedState);
            });
        });

        test('the expected success actions are dispatched', async () => {
            const data = {
                movies: [
                    {title: 'Test movie 1'},
                    {title: 'Test movie 2'}
                ],
                'total-movies': 2
            };
            const expectedActions = [
                {type: types.FETCH_MOVIES_REQUEST},
                {
                    type: types.FETCH_MOVIES_SUCCESS,
                    payload: data
                }
            ];
            moxios.wait(() => {
                const request = moxios.requests.mostRecent();
                request.respondWith({
                    status: 200,
                    response: data
                });
            });
            const store = mockStore({});
            await store.dispatch(actions.fetchMovies())
            .then(() => {
                const actualActions = store.getActions();
                expect(actualActions).toEqual(expectedActions);
            });
        });

        test('the expected failure actions are dispatched', async () => {
            const errorMessage = 'Something went wrong';
            const expectedActions = [
                {type: types.FETCH_MOVIES_REQUEST},
                {
                    type: types.FETCH_MOVIES_FAILURE,
                    payload: errorMessage
                }
            ];
            moxios.wait(() => {
                const request = moxios.requests.mostRecent();
                request.respondWith({
                    status: 500,
                    response: errorMessage
                });
            });
            const store = mockStore({});
            await store.dispatch(actions.fetchMovies())
            .catch(() => {
                const actualActions = store.getActions();
                expect(actualActions).toEqual(expectedActions);
            });

        });
    });
    
});