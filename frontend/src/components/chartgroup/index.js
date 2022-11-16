import React, {Component} from 'react';
// import Loader from '../loader';
// import Chart from '../chart';
import './styles.css';


export default class ChartGroup extends Component {

  // componentDidMount() {
  //   if (this.props.selectedGroup){
  //     this.props.setSelectedGroup(this.props.selectedGroup);
  //   }
  // }

  render() {
    // let className = this.props.className || 'btn';
    // let disabled = this.props.disabled;

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
      <div className='group-selection'>
        {this.props.groups && this.props.groups.map((group, idx) => {
          return (<button
              className= {group === this.props.selectedGroup ? "selected_button" : "unselect_button" }
              onClick = { () => {
                              console.log("Button clicked");
                              this.props.setSelectedGroup(group);
                              }

              }
              key={idx}> {group.id}. {group.name}</button>)
        })}
 
      </div>

    );
  }
}

ChartGroup.defaultProps = {
  groups : [],
  selectedGroup : null,
};
