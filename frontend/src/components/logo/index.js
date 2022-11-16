import React from 'react';
import './styles.css';

const Logo = () => {
  return (
    <div className="logoContainer">
      {/* <img src={logo} className="logo" alt="logo" /> */}
      <img src={window.location.origin + '/images/tractor.png'} className="logo" alt="logo" />
      <div className="logoTitle">Ground Controller</div>
    </div>
  );
};

export default Logo;
