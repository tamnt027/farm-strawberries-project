import React, {Component} from 'react';
import {connect} from 'react-redux';
import Navlink from '../../components/navlink';
import UserMenu from '../../components/usermenu';
import './styles.css';
import {showModal, logout} from '../../actions';

class FooterContainer extends Component {
  render() {
    const {
      isAuthenticated,
      username,
      name,
      avatar,
      handleLogout,
      isLoading,
      showRegister,
      showLogin,
      showEditProfile,
    } = this.props;

    return (
      <div className="footerContainer">
        <h5>Created by Tam</h5>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  username: state.auth.username,
  name: state.auth.name,
  avatar: state.auth.avatar,
  isAuthenticated: state.auth.isAuthenticated,
  isLoading: state.auth.isLoading,
});

const mapDispatchToProps = dispatch => ({
  handleLogout: () => {
    dispatch(logout());
  },
  showRegister: () => {
    dispatch(showModal('REGISTER', {}));
  },
  showLogin: () => {
    dispatch(showModal('LOGIN', {}));
  },
  showEditProfile: () => {
    dispatch(showModal('EDIT_PROFILE', {}));
  },
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(FooterContainer);
