import { combineReducers } from 'redux'
import actorReducer from './actor/actorReducer'

const rootReducer = combineReducers({
    actor: actorReducer
})

export default rootReducer