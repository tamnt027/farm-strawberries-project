import {
  FETCH_CHARTGROUPS_REQUEST,
  FETCH_CHARTGROUPS_SUCCESS,
  FETCH_CHARTGROUPS_FAILURE,
  SET_SELECTED_CHARTGROUP,

  FETCH_CHARTS_REQUEST,
  FETCH_CHARTS_SUCCESS,
  FETCH_CHARTS_FAILURE,
} from './types';
import {fetchGroupsApi, fetchChartsApi} from '../api';
import {apiErrorHandler} from '../utils/errorhandler';

export const fetchGroups = () => dispatch => {
  dispatch(fetchGroupsRequest());

  fetchGroupsApi()
    .then(response => {
      dispatch(fetchGroupsSuccess(response.data));
      if (response.data.length > 0) {
        dispatch(setSelectedGroupRequest(response.data[0]))
        dispatch(fetchCharts(response.data[0]))
      }
      
    })
    .catch(error => {
      const errorMessage = apiErrorHandler(error);
      dispatch(fetchGroupsFailure(errorMessage));
    });
};

export const setSelectedGroup = (group) => dispatch => {
  dispatch(setSelectedGroupRequest(group));
};


export const fetchGroupsRequest = () => {
  return {
    type: FETCH_CHARTGROUPS_REQUEST,
  };
};

export const fetchGroupsSuccess = data => {
  return {
    type: FETCH_CHARTGROUPS_SUCCESS,
    groups: data,
  };
};

export const fetchGroupsFailure = error => {
  return {
    type: FETCH_CHARTGROUPS_FAILURE,
    error,
  };
};

export const setSelectedGroupRequest = group => {
  return {
    type: SET_SELECTED_CHARTGROUP,
    selectedGroup : group,
  };
};


export const fetchCharts = (group) => dispatch => {
  dispatch(fetchChartsRequest());

  fetchChartsApi(group)
    .then(response => {
      dispatch(fetchChartsSuccess(response.data));
    })
    .catch(error => {
      const errorMessage = apiErrorHandler(error);
      dispatch(fetchChartsFailure(errorMessage));
    });
};

export const fetchChartsRequest = () => {
  return {
    type: FETCH_CHARTS_REQUEST,
  };
};

export const fetchChartsSuccess = data => {
  return {
    type: FETCH_CHARTS_SUCCESS,
    charts: data.charts,
  };
};

export const fetchChartsFailure = error => {
  return {
    type: FETCH_CHARTS_FAILURE,
    error,
  };
};