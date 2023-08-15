import { Component } from 'react'
import ReactPlayer from 'react-player'

class VideoPlayer extends Component {
    render () {
        const { videoUrl } = this.props;
        console.log(videoUrl);
        console.log('yes this is happening');
        return (
        <div className='player-wrapper'>
            <ReactPlayer
            className='react-player fixed-bottom'
            url= {"videos/" + videoUrl}
            width='100%'
            height='100%'
            controls = {true}
  
            />
        </div>
        )
    }
  }

export default VideoPlayer;