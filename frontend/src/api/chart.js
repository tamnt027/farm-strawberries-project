import axios from 'axios';
import {
  GROUP_URL,
  CHART_URL,
} from './constants';
import {getConfig} from '../utils/config';


export const fetchGroupsApi = () => {
  return axios.get(GROUP_URL, getConfig());
};

export const fetchChartsApi = (group) => {
  return axios.get(`${GROUP_URL}${group.id}/`, getConfig());
};


export const fetchChartDetailApi = (chartId) => {
  return axios.get(`${CHART_URL}${chartId}/`, getConfig());
};

// export const fetchGroupApi = thread => {
//   return axios.get(THREAD_URL + thread, getConfig());
// };


// export const fetchThreadApi = thread => {
//   return axios.get(THREAD_URL + thread, getConfig());
// };

// export const createThreadApi = newThread => {
//   return axios.post(THREAD_CREATE_URL, newThread, getConfig());
// };

// export const deleteThreadApi = id => {
//   return axios.delete(THREAD_URL + id + THREAD_DELETE_URL, getConfig());
// };

// export const editThreadApi = (id, data) => {
//   return axios.put(THREAD_URL + id + THREAD_EDIT_URL, data, getConfig());
// };
