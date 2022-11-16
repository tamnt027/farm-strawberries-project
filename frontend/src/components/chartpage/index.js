import React, {Component} from 'react';
// import Loader from '../loader';
import Chart from '../chart';
import './styles.css';


export default class ChartPage extends Component {
  render() {
    // let className = this.props.className || 'btn';
    // let disabled = this.props.disabled;

    let groupName = this.props.selectedGroup ? this.props.selectedGroup.name : "Undefined Shed" 
    groupName = groupName.replaceAll('-', ' ')

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
              <div className="flex-item">
                <Chart key={idx} {...chart} />

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
