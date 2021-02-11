import React from 'react';
import ReactDOM from 'react-dom'
import * as serviceWorker from "./reportWebVitals"
import './index.css'
import { Route, BrowserRouter as Router, Switch } from 'react-router-dom'
import App from "./App";
import Header from './components/Header'
import Footer from './components/Footer'
import ConnectionExample from './components/ConnectionExample'


const routing = (
  <Router>
      <React.StrictMode>
          <Header/>
          <Switch>
              <Route exact path="/" component={App}/> {/* Main app entry*/}
          </Switch>
          <ConnectionExample/>
          <Footer/>
      </React.StrictMode>
  </Router>
);

ReactDOM.render(routing, document.getElementById('root')); // Wyrenderuj gorny komponent w pliku
