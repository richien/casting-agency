import React from 'react';
import { shallow, mount } from 'enzyme';
import { testStore } from '../../../utils';
import RecentActorsList from '../RecentActorsList';

const initialState = {
    actors: { 
        data: [
                {id: 1, name: 'James Henry'},
                {id: 2, name: 'Jos Stan'}
            ],
        loading: false,
        error: '',
        totalItems: 0 }
}

const setUpShallow = (initialState={}, newProps={}) => {
    const props = {
        actors: [
            {id: 1, name: 'James Henry'},
            {id: 2, name: 'Jos Stan'}
        ],
        fetchActors: jest.fn(),
        loading: false
    }
    const store = testStore(initialState);
    const wrapper = shallow(<RecentActorsList store={store} {...props} {...newProps}/>).childAt(0).dive();
    return wrapper;
}

const setUpMount = (initialState={}, newProps={}) => {
    const props = {
        actors: [
            {id: 1, name: 'James Henry'},
            {id: 2, name: 'Jos Stan'}
        ],
        fetchActors: jest.fn(),
        loading: false
    }
    const store = testStore(initialState);
    const wrapper = mount(<RecentActorsList store={store} {...props} {...newProps}/>);
    return wrapper;
}


describe('RecentActorsList', () => {
    describe('Shallow render', () => {
        let wrapper;
        beforeEach(() => {
            wrapper = setUpShallow(initialState)
        });

        test('renders without errors', () => {
            const listItems = wrapper.find(`[data-test='list-wrapper']`);
            expect(listItems.length).toBe(2);
        })
    })

    describe('mount render', () => {
        let wrapper;
        beforeEach(() => {
            wrapper = setUpMount(initialState)
        });

        test('renders spinner when loading is false', () => {
            const spinnerDiv = wrapper.find(`[data-test='spinner']`);
            expect(spinnerDiv.length).toBe(1);
        })
    })


});