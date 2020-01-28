import React from 'react';
import { shallow } from "enzyme";
import Actor from '../Actor';

const setUp = () => {
    const props = {
        actor: {
            name: 'James Doe',
            id: 1
        },
        redirect: true
    };
    const wrapper = shallow(<Actor {...props}/>);
    return wrapper;
}

describe('Actor', () => {
    let wrapper;
    beforeEach(() => {
        wrapper = setUp();
    });
    test('redirects the user when redirect prop is true', () => {
        expect(wrapper.find('Redirect').prop('to')).toBe('/actors/1');
    });

    test('does not redirect the user when redirect prop is false', () => {
        wrapper.setProps({redirect: false});
        expect(wrapper.find('Redirect').length).toBe(0);
    });
    
});