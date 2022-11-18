import React, {Component} from 'react';
import {connect} from 'react-redux';
import './styles.css';


class FooterContainer extends Component {
  render() {


    return (
      <div className="footerContainer">
        <h5>Created by Tam</h5>
      </div>
    );
  }
}

const mapStateToProps = state => ({

});

const mapDispatchToProps = dispatch => ({

});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(FooterContainer);
