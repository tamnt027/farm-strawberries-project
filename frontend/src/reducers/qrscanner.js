import {
  ADD_NEW_QRCODE,
  CLEAR_ALL_QRCODE,

} from '../actions/types';

const initialState = {
  isLoading: true,
  error: null,
  results: ["default text"],
  newProps : 10,
};

const qrscanner = (state = initialState, action) => {
  switch (action.type) {
    // case FETCH_USERS_REQUEST:
    //   return {
    //     ...state,
    //     isLoading: true,
    //     error: null,
    //   };
    // case FETCH_USERS_SUCCESS:
    //   return {
    //     isLoading: false,
    //     users: action.users,
    //     error: null,
    //   };
    // case FETCH_USERS_FAILURE:
    //   return {
    //     ...initialState,
    //     error: action.error,
    //   };
    case CLEAR_ALL_QRCODE:
      return {
        ...state,
        results : [],
      };

    case ADD_NEW_QRCODE:
      return {
        ...state,
        results: [action.code, ...state.results],

      };
    default:
      return state;
  };
};

export default qrscanner;
