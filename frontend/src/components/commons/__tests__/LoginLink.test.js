import React from 'react';
import { shallow } from 'enzyme';
import LoginLink from '../LoginLink';

const setUp = () => {
    const wrapper = shallow(<LoginLink/>);
    return wrapper;
}

describe('LoginLink', () => {
    let wrapper;
    const { location } = window;
    beforeEach(() => {
        delete window.location;
        window.location = { 
            replace: jest.fn()
        };

        wrapper = setUp();
    });

    afterEach(() => {
        window.location = location;
    });

    test('should render sign in button', () => {
        expect(wrapper.find('button').length).toBe(1);
        expect(wrapper.find('button').text()).toBe('Sign In');
    });

    test('should redirect user when sign in button is clicked', () => {
        wrapper.find('button').first().simulate('click');
        expect(window.location.replace).toHaveBeenCalledTimes(1);
    });
});