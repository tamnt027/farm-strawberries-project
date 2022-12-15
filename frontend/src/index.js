import React, {Fragment} from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import 'semantic-ui-css/semantic.min.css';
import {Provider} from 'react-redux';
import {BrowserRouter, Switch, Route} from 'react-router-dom';
import {PersistGate} from 'redux-persist/integration/react';
import Loader from './components/loader';
import store, {persistor} from './store';
import HeaderContainer from './containers/header';
import FooterContainer from './containers/footer'
import ModalContainer from './containers/modal';
// import UserProfileContainer from './containers/userprofile';
// import UsersContainer from './containers/users';

import HomeContainer from './containers/home';
import QRScannerContainer from './containers/qrscanner'
import NotFoundPage from './components/notfoundpage';
import ChartsContainer from './containers/charts'
import registerServiceWorker from './registerServiceWorker';
import UserProfileContainer from './containers/userprofile'
import UsersContainer from './containers/users'

ReactDOM.render(
  <Provider store={store}>
    <PersistGate loading={<Loader />} persistor={persistor}>
      <BrowserRouter>
        <Fragment>
          <header className="header-background" />
          <div className="app-layout">
            <HeaderContainer />
            <Switch>
              <Route path="/charts" component={ChartsContainer} />
              <Route path="/user/:username" component={UserProfileContainer} />
              <Route path="/users" component={UsersContainer} />
              {/* <Route path="/users" component={UsersContainer} />
              
              <Route path="/forum/:forum" component={ForumContainer} />
              <Route path="/thread/:thread" component={ThreadContainer} /> */}
              <Route exact path="/qrscanner" component={QRScannerContainer} />
              <Route exact path="/" component={HomeContainer} />
              <Route component={NotFoundPage} />
            </Switch>
            <FooterContainer />
          </div>
          <ModalContainer />
        </Fragment>
      </BrowserRouter>
    </PersistGate>
  </Provider>,
  document.getElementById('root'),
);
registerServiceWorker();
