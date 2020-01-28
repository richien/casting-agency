import React from 'react';
import { shallow, mount } from 'enzyme';
import Dashboard from './Dashboard';

const setUp = () => {
    const wrapper = shallow(<Dashboard/>);
    return wrapper;
}

describe('Dasboard', () => {
    let wrapper;
    beforeEach(() => {
        wrapper = setUp();
    });

    test('should not render the component when a user is  not authenticated', () => {
        expect(wrapper.find('.content-wrapper').length).toBe(0);
        expect(wrapper.find('Redirect').prop('to')).toBe('/');;
    });
});