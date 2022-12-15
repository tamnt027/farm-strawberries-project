import React, {Component} from 'react';
import {Message, Image} from 'semantic-ui-react';
import './styles.css';

class NotAllowPage extends Component {
  render() {
    return (
      <div>
        <div className="not-found-page">
          <Message>
            <Message.Content>
              <Message.Header>401 - Unauthorized</Message.Header>
              Sorry, you are unauthorized to view this page.
            </Message.Content>
          </Message>
        </div>
        <Image
          className="not-found-page-img"
          src={window.location.origin + '/images/notallow.gif'}
          centered
        />
      </div>
    );
  }
}
export default NotAllowPage;
