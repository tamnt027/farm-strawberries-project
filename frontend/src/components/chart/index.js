import React, {Component} from 'react';
// import Loader from '../loader';
// import './styles.css';
import Plot from 'react-plotly.js';


export default class Chart extends Component {


  componentWillMount() {
    // const {id} = this.props
    // console.log(`load chart id ${id}`);
    // this.props.fetchChart(id);
    // const chartDetail = fetchChartDetailApi(id);

    // // this.data = data
    // // this.config = config
    // // this.frames = frames
    // // this.layout = layout
    
    // console.log(chartDetail)
  }

  render() {
    // let className = this.props.className || 'btn';
    // let disabled = this.props.disabled;

    // if (this.props.loading) {
    //   disabled = true;
    // }
    const {id, data, config, frames, layout} = this.props
    console.log(`render  chart ${id}`)
    return (
      <>
      {/* <p>{id}</p> */}
      <Plot
        data={data}
        config= {config}
        frames= {frames}
        layout={layout}
        useResizeHandler={true}
        style={{width: "100%", height: "100%"}}
      />
      </>
    );
  }
}

Chart.defaultProps = {
  data : {},
  layout: {},
  config: {},
  frames: [],
};
