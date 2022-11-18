import {
  // FETCH_USERS_REQUEST,
  // FETCH_USERS_SUCCESS,
  // FETCH_USERS_FAILURE,
  ADD_NEW_QRCODE,
  CLEAR_ALL_QRCODE,
} from './types';
// import {fetchUsersApi} from '../api';
// import {apiErrorHandler} from '../utils/errorhandler';

// export const fetchUsers = () => dispatch => {
//   dispatch(fetchUsersRequest());

//   fetchUsersApi()
//     .then(response => {
//       dispatch(fetchUsersSuccess(response.data));
//     })
//     .catch(error => {
//       const errorMessage = apiErrorHandler(error);
//       dispatch(fetchUsersFailure(errorMessage));
//     });
// };

// export const fetchUsersRequest = () => {
//   return {
//     type: FETCH_USERS_REQUEST,
//   };
// };

// export const fetchUsersSuccess = data => {
//   return {
//     type: FETCH_USERS_SUCCESS,
//     users: data,
//   };
// };

// export const fetchUsersFailure = error => {
//   return {
//     type: FETCH_USERS_FAILURE,
//     error,
//   };
// };

export const addQRCode = newCode => {
  return {
    type : ADD_NEW_QRCODE,
    code : newCode,
  };
};

export const clearAllQRCodes = () => {
  return {
    type : CLEAR_ALL_QRCODE,
  }
}

export const initQRCode = () => {
  return {
    
  }
}