import React from 'react';
import { shallow } from 'enzyme';
import LogoutLink from '../LogoutLink';
import 'jest-localstorage-mock';

const setUp = () => {
    const wrapper = shallow(<LogoutLink/>);
    return wrapper;
}

describe('LogoutLink', () => {
    let wrapper;
    beforeEach(() => {
        wrapper = setUp();
    });
    test('should render sign out button', () => {
        expect(wrapper.find('button').length).toBe(1);
        expect(wrapper.find('button').text()).toBe('Sign Out');
    });

    test('should redirect user when sign out button is clicked', () => {
        let windowSpy = jest.spyOn(global, 'window', 'get');
        windowSpy.mockImplementation(() => ({
            location: {
                replace: jest.fn()
            }
        }));
        
        wrapper.find('button').first().simulate('click');
        expect(localStorage.clear).toHaveBeenCalledTimes(1);
        windowSpy.mockRestore();
    });
});