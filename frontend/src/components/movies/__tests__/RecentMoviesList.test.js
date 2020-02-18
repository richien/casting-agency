import React from 'react';
import { shallow, mount } from 'enzyme';
import { testStore } from '../../../utils';
import RecentMoviesList from '../RecentMoviesList';

const initialState = {
    movies: {
        data: [
            {id: 1, title: 'Test movie 1'},
            {id: 2, title: 'Test movie 2'}
        ],
        loading: false,
        error: '',
        totalItems: 2
    }
}

const setUpShallow = (state={}) => {
    const props = {
        movies: [
            {id: 1, title: 'Test movie 1'},
            {id: 2, title: 'Test movie 2'}
        ],
        fetchMovies: jest.fn(),
        loading: false
    };
    const store = testStore(state);
    const wrapper = shallow(<RecentMoviesList store={store} {...props}/>).childAt(0).dive();
    return wrapper;
};

const setUpMount = (state={}) => {
    const props = {
        movies: [
            {id: 1, title: 'Test movie 1'},
            {id: 2, title: 'Test movie 2'}
        ],
        fetchMovies: jest.fn(),
        loading: false
    };
    const store = testStore(state);
    const wrapper = mount(<RecentMoviesList store={store} {...props}/>);
    return wrapper;
};

describe('RecentMoviesList', () => {
    describe('shallow render', () => {
        let wrapper;
        beforeEach(() => {
            wrapper = setUpShallow(initialState);
        });

        test('renders without errors', () => {
            const listItems = wrapper.find(`[data-test='list-wrapper']`);
            expect(listItems.length).toBe(2);
        });

        test('sets redirect to true when an item clicked', () => {
            wrapper.find(`[data-test='list-wrapper']`).first().simulate('click');
            expect(wrapper.find('Movie').first().prop('redirect')).toBeTruthy();
        });
    });

    describe('mount render', () => {
        let wrapper;
        beforeEach(() => {
            wrapper = setUpMount(initialState);
        });
        
        test('renders spinner when loading is false', () => {
            const spinnerDiv = wrapper.find(`[data-test='spinner']`);
            expect(spinnerDiv.length).toBe(1);
        });
    });
});