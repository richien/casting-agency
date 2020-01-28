import React from 'react';
import { shallow } from 'enzyme';
import LoginRedirect from '../LoginRedirect';
import 'jest-localstorage-mock';

const setUp = () => {
    const wrapper = shallow(<LoginRedirect/>);
    return wrapper;
}

describe('LoginRedirect', () => {
    let wrapper;
    const { location } = window;

    beforeEach(() => {
        delete window.location;
        window.location = { 
            replace: jest.fn(), 
            hash: '#access_token=sample-token' 
        };
        wrapper = setUp();
    });

    afterEach(() => {
        window.location = location;
    });

    test('should render spinner before redirect', () => {
        expect(wrapper.find('Spinner').length).toBe(1);
    });

    test('should store token in localstorage', () => {
        expect(localStorage.getItem('JWT_TOKEN')).toBe('sample-token');
    });

    test('should set isAuthenticated to true in localstorage', () => {
        expect(localStorage.getItem('isAuthenticated')).toEqual('true');
    });
    
    test('should redirect the user to the dashboard page', () => {
        expect(window.location.replace).toHaveBeenCalledTimes(1);
        expect(window.location.replace).toHaveBeenCalledWith('/dashboard');
    });

});