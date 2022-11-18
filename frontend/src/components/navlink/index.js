import React from 'react';
import Logo from '../logo';
import {Link} from 'react-router-dom';
import {Icon} from 'semantic-ui-react';
import './styles.css';

const Navlink = () => {
  return (
    <div className="navlinkContainer">
      <Logo />
      <div className="link">
        <Icon name="home" className="navlinkIcon" />
        <Link to="/">Home</Link>
      </div>

      <div className="link">
        <Icon name="chart line" className="navlinkIcon" />
        <Link to="/charts">Charts</Link>
      </div>
      <div className="link">
        <Icon name="camera" className="navlinkIcon" />
        <Link to="/qrscanner">QR Scanner</Link>
      </div>
      {/* <div className="link">
        <Icon name="users" className="navlinkIcon" />
        <Link to="/users">Users</Link>
      </div> */}
      {/* <div className="link">
        <Icon name="github" className="navlinkIcon" />
        <a href="https://github.com/tamnt027">GitHub</a>
      </div> */}
    </div>
  );
};

export default Navlink;
