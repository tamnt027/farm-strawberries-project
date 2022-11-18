import React, {Component} from 'react';
import {connect} from 'react-redux';
import QRScanner from '../../components/qrscanner';
import {addQRCode, clearAllQRCodes} from '../../actions';
class QRScannerContainer extends Component {

  render() {
    // const {results} = this.props.results;
    return (<>
          <QRScanner {...this.props} />

        </>
    );
  }


}


// isLoading: true,
// error: null,
// results: ["default text"],
// newProps : 10,

const mapStateToProps = state => ({
  isLoading: state.qrscanner.isLoading,
  error: state.qrscanner.error,
  results : state.qrscanner.results,
  
});

const mapDispatchToProps = dispatch => ({
  addNewQRCode: (newCode) => {
    dispatch(addQRCode(newCode));
  },
  clearAllQRCodes : () => {
    dispatch(clearAllQRCodes());
  },
});

// export default QRScannerContainer
export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(QRScannerContainer);
