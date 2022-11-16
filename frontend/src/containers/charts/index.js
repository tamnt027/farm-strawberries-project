import React, {Component} from 'react';
import {connect} from 'react-redux';
import {fetchGroups, setSelectedGroup, fetchCharts} from '../../actions';
// import UserList from '../../components/userlist';
import ChartPage from '../../components/chartpage'
import ChartGroup from '../../components/chartgroup';

class ChartsContainer extends Component {
  componentDidMount() {
     this.props.fetchGroups();
  }

  render() {

    return (
    <>
      <ChartGroup {...this.props} />
      <ChartPage {...this.props} />
    </>
    
    );
    // return (<h1>Chart page</h1>)
  }
}

const mapStateToProps = state => ({  // state is global root state.
  isLoading: state.groups.isLoading,
  groups: state.groups.groups,
  error: state.groups.error,
  selectedGroup : state.groups.selectedGroup,
  charts: state.groups.charts,
});

const mapDispatchToProps = dispatch => ({
  fetchGroups: () => {
    dispatch(fetchGroups());
  },
  setSelectedGroup: group => {
    dispatch(setSelectedGroup(group));
    dispatch(fetchCharts(group));
  },
  fetchCharts: (group) => {
    dispatch(fetchCharts(group));
  }, 

});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(ChartsContainer);
