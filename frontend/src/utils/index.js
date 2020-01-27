import { applyMiddleware, createStore } from 'redux';
import { middlewares } from '../store';
import rootReducer from '../redux/rootReducer';
import configureMockStore from 'redux-mock-store';

export const testStore = (initialState) => {
    const createStoreWithMiddlware = applyMiddleware(...middlewares)(createStore);
    return createStoreWithMiddlware(rootReducer, initialState);
}

export const mockStore = configureMockStore(middlewares)