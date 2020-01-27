import { createStore, applyMiddleware } from 'redux'
import rootReducer from './redux/rootReducer'
import { composeWithDevTools } from 'redux-devtools-extension'
import thunk from 'redux-thunk'

export const middlewares = [thunk]
const store = createStore(
    rootReducer,
    composeWithDevTools(applyMiddleware(...middlewares))
)

export default store