import { combineReducers } from 'redux'
import fetchActorsReducer from './actor/reducers/fetchActorsReducer'

const rootReducer = combineReducers({
    actors: fetchActorsReducer
})

export default rootReducer