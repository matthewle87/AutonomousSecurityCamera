import { Component } from 'react'
import ReactPlayer from 'react-player'

class VideoPlayer extends Component {
    render () {
        const { videoUrl } = this.props;
        const time = videoUrl.split(/[-.]/);
        return (
        <div className='player-wrapper'>
            <ReactPlayer
            className='react-player fixed-bottom'
            url= {"videos/" + videoUrl}
            width='100%'
            height='100%'
            controls = {true}
            />
            {`${time[1]}/${time[0]}/${time[2]} ${time[3]}:${time[4]}:${time[5]}`}
        </div>
        )
    }
  }

export default VideoPlayer;