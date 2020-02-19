import { applyMiddleware, createStore } from 'redux';
import { middlewares } from '../store';
import rootReducer from '../redux/rootReducer';
import configureMockStore from 'redux-mock-store';
import config from '../auth_config.json';

export const testStore = (initialState) => {
    const createStoreWithMiddlware = applyMiddleware(...middlewares)(createStore);
    return createStoreWithMiddlware(rootReducer, initialState);
}

export const mockStore = configureMockStore(middlewares)

export const doLogout = () => {
    let logOutLink = `https://${config.domain}/v2/logout?&returnTo=${config.logoutRedirect}&client_id=${config.clientId}`;
    localStorage.clear();
    return window.location.replace(logOutLink);
}