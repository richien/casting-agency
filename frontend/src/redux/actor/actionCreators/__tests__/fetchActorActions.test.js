import moxios from 'moxios';
import { testStore, mockStore } from '../../../../utils';
import * as actions from '../../../actor';
import * as types from '../../actorTypes';

describe('FetchActorActions', () => {

    describe('asynchronous action creators', () => {
        beforeEach(() => {
            moxios.install();
        });

        afterEach(() => {
            moxios.uninstall();
        });

        test('store is updated correctly', async () => {
            const data = {
                actors: [
                            {
                                name: 'Test 1',
                                age: 23
                            },
                            {
                                name: 'Test 2',
                                age: 24
                            }
                        ],
                'total-actors': 2
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
                data: data.actors,
                totalItems: data['total-actors'],
                error: ''
            }
            await store.dispatch(actions.fetchActors()).then(()=> {
                    const newState = store.getState()['actors'];
                    expect(newState).toEqual(expectedState);
                })
        });

        test('the expected success actions are dispatched', async () => {
            const data = {
                actors: [
                            {
                                name: 'Test 1',
                                age: 23
                            },
                            {
                                name: 'Test 2',
                                age: 24
                            }
                        ],
                'total-actors': 2
            };
            const expectedActions = [
                {
                    type: types.FETCH_ACTORS_REQUEST
                },
                {
                    type: types.FETCH_ACTORS_SUCCESS,
                    payload: data
                }
            ]

            moxios.wait(() => {
                const request = moxios.requests.mostRecent();
                request.respondWith({
                    status: 200,
                    response: data
                });
            });

            const store = mockStore({});
            await store.dispatch(actions.fetchActors())
            .then(() => {
                const actualActions = store.getActions()
                expect(actualActions).toEqual(expectedActions)
            })
        });

        test('the expected failure actions are dispatched', async () => {
            const errorMessage = 'Test Resource Not Found';
            const expectedActions = [
                {
                    type: types.FETCH_ACTORS_REQUEST
                },
                {
                    type: types.FETCH_ACTORS_FAILURE,
                    payload: errorMessage
                }
            ]

            moxios.wait(() => {
                const request = moxios.requests.mostRecent();
                request.respondWith({
                    status: 404,
                    response: errorMessage
                });
            });

            const store = mockStore({});
            
            await store.dispatch(actions.fetchActors())
            .catch(error => {
                console.log('ERROR - ', error)
                const actualActions = store.getActions()
                expect(actualActions).toEqual(expectedActions)
            })
                
        });

    })

    describe('synchronous action creators', () => {
        test('returns the request action', () => {

            const expectedAction = {
                type: types.FETCH_ACTORS_REQUEST
            }

            const actualAction = actions.fetchActorsRequest()

            expect(actualAction).toEqual(expectedAction);
        });

        test('returns the success action', () => {
            const data = {
                actors: [],
                'total-items': 0
            }
            const expectedAction = {
                type: types.FETCH_ACTORS_SUCCESS,
                payload: data
            }

            const actualAction = actions.fetchActorsSuccess(data)

            expect(actualAction).toEqual(expectedAction);
        });

        test('returns the failure action', () => {
            const errorMessage = 'An error occured'
            const expectedAction = {
                type: types.FETCH_ACTORS_FAILURE,
                payload: errorMessage
            }

            const actualAction = actions.fetchActorsFailure(errorMessage)

            expect(actualAction).toEqual(expectedAction);
        });
    });
    
})