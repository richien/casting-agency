import React from 'react';
import { Provider } from 'react-redux'
import store from './store'
import './App.css';
import './assets/css/styles.css'
import NavBarContainer from './components/commons/NavBarContainer';
import 'materialize-css/dist/css/materialize.min.css'
import Routes from './routes/Routes';
import FooterContainer from './components/commons/FooterContainer';
import { useAuth0 } from './components/containers/ReactAuth0Spa';
import Spinner from './components/commons/Spinner'

function App() {
  const { loading } = useAuth0()

  return (
    <div className="AppWrapper">
      {loading && ( 
        <div id="lp-spinner">
            <Spinner/>
        </div> )}
      {!loading &&
        (<Provider store={store}>
        <div className="App">
          <NavBarContainer />
          <Routes />
          <FooterContainer />
        </div>
      </Provider>
      )}
    </div>
  );
}

export default App;
