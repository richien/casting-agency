import React from 'react';
import { shallow } from 'enzyme';
import Profile from './Profile';


const setUp = () => {
    const props = {
        user: {
            name: 'Gaf Higgins',
            picture: 'my-pic.png'
        }
    }
    return shallow(<Profile {...props}/>);
}

describe('Profile', () => {
    let wrapper;
    beforeEach(() => {
        wrapper = setUp();
    });
    test("should render the user's profile image", () => {
        console.log(wrapper.debug());
        expect(wrapper.find('img').prop('src')).toBe('my-pic.png');
    });

    test("should render the user's name", () => {
        expect(wrapper.find(`[data-test='username']`).text()).toBe('Gaf Higgins');
    });
});