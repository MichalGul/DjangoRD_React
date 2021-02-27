import React from 'react';
import ReactDOM from 'react-dom'
import * as serviceWorker from "./reportWebVitals"
import './index.css'
import { Route, BrowserRouter as Router, Switch } from 'react-router-dom'
import App from "./App";
import Header from './components/Header'
import Footer from './components/Footer'
import SignUp from './components/register'
import SignIn from './components/login'
import SignOut from './components/logout'
import Single from './components/single'
import Material from './components/material'
import ConnectionExample from './components/ConnectionExample'
import {ThemeProvider} from "@material-ui/core/styles";
import theme from "./theme";

const routing = (
  <Router>
      <React.StrictMode>
          <ThemeProvider theme={theme}>
              <Header/>
              <Switch>
                  <Route exact path="/" component={App}/> {/* Main app entry*/}
                  <Route path="/register" component={SignUp} />
                  <Route path="/login" component={SignIn} />
                  <Route path="/logout" component={SignOut} />
                  <Route path="/post/:slug" component={Single} />
                  <Route path="/material-ui" component={Material} />
              </Switch>
              <ConnectionExample/>
              <Footer/>
          </ThemeProvider>
      </React.StrictMode>
  </Router>
);

ReactDOM.render(routing, document.getElementById('root')); // Wyrenderuj gorny komponent w pliku
