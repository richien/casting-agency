import { combineReducers } from 'redux';
import fetchActorsReducer from './actor/reducers/fetchActorsReducer';
import fetchMoviesReducer from './movie/reducers/fetchMoviesReducer';

const rootReducer = combineReducers({
    actors: fetchActorsReducer,
    movies: fetchMoviesReducer
})

export default rootReducer