import React, { useState, useEffect } from 'react'
import axios from "axios";
import logo from './logo.svg';
import './App.css';
import VideoPlayer from './VideoPlayer'

function App() {

  const [videoNames, setVideoNames] = useState(null);
  const [selectedVideo, setSelectedVideo] = useState(null);
  
  function showVideo(vidName){
    console.log(vidName)
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
      res.videos.forEach(vid => {
        console.log(vid);
      });
    })
    .catch((error) => {
      if (error.response) {
        console.log(error.response);
        console.log(error.response.status);
        console.log(error.response.headers);
      }
    });
  }, []);


  return (




    <div className="App">
      <div className = 'videoButtons'>
        {videoNames && videoNames.videos.map((videoName, index) => (
          <button 
            key={index} 
            className = 'button'
            onClick ={() => showVideo(videoNames.videos[index])}>
            {videoName}
          </button>
        ))}
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