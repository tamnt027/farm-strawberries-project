import React, {Component} from 'react';
// import Loader from '../loader';
import './styles.css';

import { Html5QrcodeScanner } from "html5-qrcode";

const qrcodeRegionId = "html5qr-code-full-region";

class Html5QrcodePlugin  extends Component {
  render() {
    return <div id={qrcodeRegionId} style={{width: "500px", margin: "auto"}}/>;
  }

  componentWillUnmount() {
      // TODO(mebjas): See if there is a better way to handle
      //  promise in `componentWillUnmount`.
      this.html5QrcodeScanner.clear().catch(error => {
          console.error("Failed to clear html5QrcodeScanner. ", error);
      });
  }

  componentDidMount() {
      // Creates the configuration object for Html5QrcodeScanner.
      function createConfig(props) {
          var config = {};
          if (props.fps) {
          config.fps = props.fps;
          }
          if (props.qrbox) {
          config.qrbox = props.qrbox;
          }
          if (props.aspectRatio) {
          config.aspectRatio = props.aspectRatio;
          }
          if (props.disableFlip !== undefined) {
          config.disableFlip = props.disableFlip;
          }
          return config;
      }

      var config = createConfig(this.props);
      var verbose = this.props.verbose === true;

      // // Suceess callback is required.
      // if (!(this.props.qrCodeSuccessCallback )) {
      //     throw "qrCodeSuccessCallback is required callback.";
      // }

      this.html5QrcodeScanner = new Html5QrcodeScanner(
          qrcodeRegionId, config, verbose);
      this.html5QrcodeScanner.render(
          this.props.qrCodeSuccessCallback,
          this.props.qrCodeErrorCallback);
  }
}




export default class QRScanner extends Component {

  constructor(props) {
    super(props);
    
    // This binding is necessary to make `this` work in the callback.
    this.onNewScanResult = this.onNewScanResult.bind(this);
    // this.props.addNewQRCode("NewONe");
  }

  componentDidMount() {
    this.props.clearAllQRCodes();
  }

  onNewScanResult(decodedText, decodedResult) {
      console.log(decodedText);
      const nowTime = new Date().toLocaleTimeString();
      // const newDate = new Date();
      // const datetime = newDate.today() + " @ " + newDate.timeNow() + " ";
      this.props.addNewQRCode( `${nowTime}: ${decodedText}`);

    }

  render() {


    return (
      <>
        <h1>QR Scanner</h1>
        <Html5QrcodePlugin 
              fps={10}
              qrbox={{width: 250, height: 250 }}
              disableFlip={false}
              qrCodeSuccessCallback={this.onNewScanResult}/>
        <h2>Scanned Result List</h2>
        <ul className={"scanned-list"}>
          {this.props.results && this.props.results.map((resultx, idx) => {
      
            return (
              <li key={idx} className={"scanned-item"}>
                {resultx}

              </li>
            )

          })}

        </ul>
      </>

      // <Chart

      // />
    );
  }
}

// ChartPage.defaultProps = {
//   charts : [],
//   // className: 'btn',
//   // type: 'submit',
//   loading: false,
//   disabled: false,
//   onClick: null,
// };
