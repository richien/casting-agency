import React from 'react';
import { Provider } from 'react-redux'
import store from './store'
import './App.css';
import './assets/css/styles.css'
import 'materialize-css/dist/css/materialize.min.css'
import Routes from './routes/Routes';

function App() {
  return (
    <div className="AppWrapper">
      <Provider store={store}>
        <div className="App">
          <Routes />
        </div>
      </Provider>
    </div>
  );
}

export default App;
