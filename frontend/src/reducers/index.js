import {combineReducers} from 'redux';
import auth from './auth';
import modal from './modal';
import register from './register';
import userProfile from './userprofile';
import home from './home';
import users from './users';
import forum from './forum';
import thread from './thread';
import groups from './charts';
import qrscanner from './qrscanner';

const rootReducer = combineReducers({
  auth,
  modal,
  register,
  userProfile,
  home,
  users,
  forum,
  thread,
  groups,
  qrscanner,
});

export default rootReducer;
