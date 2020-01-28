import React from 'react';
import { shallow } from 'enzyme';
import NavBar from './NavBar';

const setUp = () => {
    const wrapper = shallow(<NavBar/>);
    return wrapper
}

describe('NavBar', () => {
    let wrapper;
    beforeEach(() => {
        wrapper = setUp();
    });
    describe('unauthenticated user', () => {
        test('should render the LoginLink component when unauthenticated', () => {
            expect(wrapper.find('LoginLink').length).toBe(1);
        });
    });
    
});