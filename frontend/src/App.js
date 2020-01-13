import React from 'react';
import { Provider } from 'react-redux'
import store from './store'
import './App.css';
import './assets/css/styles.css'
import NavBarContainer from './components/commons/NavBarContainer';
import 'materialize-css/dist/css/materialize.min.css'
import Routes from './routes/Routes';
import FooterContainer from './components/commons/FooterContainer';

function App() {
  return (
    <Provider store={store}>
      <div className="App">
        <NavBarContainer />
        <Routes />
        <FooterContainer />
      </div>
    </Provider>
  );
}

export default App;
