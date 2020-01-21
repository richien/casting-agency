import { combineReducers } from 'redux'
import actorReducer from './actor/reducers/fetchActorsReducer'

const rootReducer = combineReducers({
    actor: actorReducer
})

export default rootReducer