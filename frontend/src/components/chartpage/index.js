import React, {Component} from 'react';
// import Loader from '../loader';
import Chart from '../chart';
import './styles.css';
import StatusMessage from '../statusmessage';

export default class ChartPage extends Component {
  render() {
    // let className = this.props.className || 'btn';
    // let disabled = this.props.disabled;
    const {isLoading, error} = this.props;
    let groupName = this.props.selectedGroup ? this.props.selectedGroup.name : "Undefined Shed" 
    groupName = groupName.replaceAll('-', ' ')


    if (error ||  isLoading  ) {
      return (
        <StatusMessage
          error={error }
          errorClassName="home-error"
          errorMessage={error}
          loading={isLoading}
          loadingMessage={'We are fetching the charts for you'}
          // nothing={forums && forums.length === 0}
          nothingMessage={'No Charts to display'}
          nothingClassName="home-error"
          type="default"
        />
      );
    }
    // if (this.props.loading) {
    //   disabled = true;
    // }

    return (
      // <button
      //   className={className}
      //   disabled={disabled}
      //   onClick={this.props.onClick}
      //   type={
      //     this.props.type
      //       ? this.props.type
      //       : this.props.onClick
      //         ? 'button'
      //         : 'submit'
      //   }>
      //   {this.props.loading ? <Loader /> : this.props.children}
      // </button>
      <>
      <h1>{groupName}</h1>
      <div className="flex-container" >
        {this.props.charts &&this.props.charts.map((chart, idx) => {
    
            return (
              <div className="flex-item" key={idx}>
                <Chart  {...chart} />

              </div>
            )
        
        })}

      </div>

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
