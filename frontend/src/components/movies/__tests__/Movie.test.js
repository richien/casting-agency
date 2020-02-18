import React from 'react';
import { shallow } from 'enzyme';
import Movie from '../Movie';

const setUp = () => {
    const props = {
        movie: {
            title: 'Test Movie 1',
            id: 1
        },
        redirect: true
    };
    const wrapper = shallow(<Movie {...props}/>);
    return wrapper;
}

describe('Movie', () => {
    let wrapper;
    beforeEach(() => {
        wrapper = setUp();
    });

    test('redirects the user when the redirect prop is true', () => {
        expect(wrapper.find('Redirect').prop('to')).toBe('/movies/1');
    });
    test('does not redirect when the redirect prop is false', () => {
        wrapper.setProps({redirect: false});
        expect(wrapper.find('Redirect').length).toBe(0);
    });
});