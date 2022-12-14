import {
  FETCH_CHARTGROUPS_REQUEST,
  FETCH_CHARTGROUPS_SUCCESS,
  FETCH_CHARTGROUPS_FAILURE,
  SET_SELECTED_CHARTGROUP,
  FETCH_CHARTS_REQUEST,
  FETCH_CHARTS_SUCCESS,
  FETCH_CHARTS_FAILURE,
  FETCH_CHART_SUCCESS,

} from '../actions/types';

const initialState = {
  isLoading: false,
  groups: null,
  error: null,
  selectedGroup: null,
  charts: null,
};

const groups = (state = initialState, action) => {
  switch (action.type) {
    case FETCH_CHARTGROUPS_REQUEST:
      return {
        ...state,
        isLoading: true,
        error: null,
      };
    case FETCH_CHARTGROUPS_SUCCESS:
      return {
        isLoading: false,
        groups: action.groups,
        error: null,
      };

    case FETCH_CHARTGROUPS_FAILURE:
      return {
        ...initialState,
        error: action.error,
      };

    case SET_SELECTED_CHARTGROUP:
      return {
        ...state,
        selectedGroup : action.selectedGroup,
      }

    case FETCH_CHARTS_REQUEST:
      return {
        ...state,
        isLoading: true,
        error: null,
      };

    case FETCH_CHARTS_SUCCESS:
      return {
        ...state,
        isLoading: false,
        charts: action.charts,
        error: null,
      };

    case FETCH_CHARTS_FAILURE:
      return {
        ...state,
        isLoading: false,
        charts: [],
        error: action.error,
      };

    case FETCH_CHART_SUCCESS:
      const fetchedChart = action.fetchedChart
      // console.log(fetchedChart)
      // const newState =  {
      //   ...state,
      //   charts : this.state.charts.map(el => (el.id === fetchedChart.id ? {...el, fetchedChart} : el)),
      //   // charts:  action.fetchedChart
      // };
      console.log("FetchedChart")
      console.log(fetchedChart)

      // return state.map(product => {
      //   if (product.name === action.payload.name) {
      //     return {...product, quantity: product.quantity-1}
      //   };
      //   return product;
      // });

      return {
        ...state,
        charts : state.charts.map(el => (el.id === fetchedChart.id ? {...el, ...fetchedChart} : el)),
      };

    default:
      return state;

  }
};

export default groups;