import React, {Component} from 'react';
// import Loader from '../loader';
// import './styles.css';
import Plot from 'react-plotly.js';

export default class Chart extends Component {
  render() {
    // let className = this.props.className || 'btn';
    // let disabled = this.props.disabled;

    // if (this.props.loading) {
    //   disabled = true;
    // }
    const {data, config, frames, layout} = this.props
    console.log(`Render chart ${this.props.id}`)
    return (
      
      <Plot
        data={data}
        config= {config}
        frames= {frames}
        layout={ layout}
        useResizeHandler={true}
        style={{width: "100%", height: "100%"}}
      />
    );
  }
}

Chart.defaultProps = {
  data : {},
  layout: {},
  config: {},
  frames: [],
};
