import React from 'react';
import { shallow } from 'enzyme';
import SideMenuLinks from '../SideMenuLinks';

const setUp = () => {
    const wrapper = shallow(<SideMenuLinks />);
    return wrapper;
}

describe('SideMenuLinks', () => {
    test('should render sidebar links', () => {
        let wrapper = setUp();
        expect(wrapper.find('Link').length).toBe(2);
    });
});