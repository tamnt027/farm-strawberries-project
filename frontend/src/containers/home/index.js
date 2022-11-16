import React, {Component} from 'react';
import {connect} from 'react-redux';
// import {fetchForums} from '../../actions';
// import ForumList from '../../components/forumlist';




class Iframe extends Component {
  iframe () {
    return {
      __html: this.props.iframe
    }
  }

  render() {
    return (
      <div>
        <div dangerouslySetInnerHTML={ this.iframe() } />
      </div>
    );
  }
};

const iframe = '<iframe src="https://www.facebook.com/plugins/video.php?height=476&href=https%3A%2F%2Fwww.facebook.com%2F467.Russell.Farm%2Fvideos%2F563817858553600%2F&show_text=false&width=380&t=0" width="600" height="800" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share" allowFullScreen="true"></iframe>'; 



class HomeContainer extends Component {
  componentDidMount() {
    // this.props.fetchForums();
  }

  render() {
    return (
      <>
      <h1>Welcome to Farm Strawberries</h1>
      <div className='intro-video' style={{margin: 'auto', width: '100%', display: "flex", justifyContent: "center"}}>
        <Iframe iframe={iframe} />
      </div>
      
      </>
    );
  }
}

const mapStateToProps = state => ({
  isLoading: state.home.isLoading,
  forums: state.home.forums,
  error: state.home.error,
});

const mapDispatchToProps = dispatch => ({
  fetchForums: () => {
    // dispatch(fetchForums());
  },
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(HomeContainer);
