import React, { useState, useEffect } from 'react'
import axios from "axios";
import './App.css';
import VideoPlayer from './VideoPlayer.js'
import SearchBar from './SearchBar.jsx'

function App() {

  const [videoNames, setVideoNames] = useState(null);
  const [selectedVideo, setSelectedVideo] = useState(null);
  const [searchQuery, setSearchQuery] = useState('');
  
  function showVideo(vidName){
    setSelectedVideo(vidName);
  }

  
  useEffect(() => {
    axios({
      method: "GET",
      url: "/getall",
    })
    .then((response) => {
      const res = response.data;
      setVideoNames({
        videos: res.videos.reverse()
      });
      if (res.videos.length > 0){
        showVideo(res.videos[0])
      }
    })
    .catch((error) => {
      if (error.response) {
        console.log(error.response);
        console.log(error.response.status);
        console.log(error.response.headers);
      }
    });
  }, []);

  const filteredVideos = videoNames?.videos.filter((videoName) =>
  videoName.toLowerCase().includes(searchQuery.toLowerCase())
  ) || [];

  return (




    <div className="App">

      <div className = 'videoButtons'>
        <SearchBar searchQuery={searchQuery} setSearchQuery={setSearchQuery}/>
        {filteredVideos && filteredVideos.map((videoName, index) => {
            const time = videoName.split(/[-.]/);

            return (
              <button
                key={index}
                className="button"
                onClick={() => showVideo(videoName)}
              >
                Motion Detected
                <br />
                {`${time[1]}/${time[0]}/${time[2]}`}
                <br />
                {`${time[3]}:${time[4]}:${time[5]}`}
              </button>
            );
          })}
        </div>
      {selectedVideo && (
        <div className = 'displayedVideo'>
          <VideoPlayer videoUrl={selectedVideo} />
        </div>
      )}
    </div>
  );
}




export default App;