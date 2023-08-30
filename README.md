A program that takes in a video feed and uses AI to detect faces/bodies and begins recording, sending it to a backend server that communicates it to the frontend website, allowing for easy storage and traversal of footage.

Demo:


https://github.com/paritytech/polkadot-sdk/assets/111463817/ce33a882-1987-47ad-bc3e-1447b1437df5



Requirements:
"pip install opencv-python"
"pip install -r requirements.txt"


How to use:
1. cd into downloaded GitHub Folder and run "python backend.py"
2. Run securitycam.py and let the video stream watch for movement and ensure that the working directory is in AutonomousSecurityCamera/FRONTEND/flask_react/public/videos so that videos will be saved in there.
3. cd "FRONTEND/flask_react" and run "npm start". If there are videos present in the current directory, then they will be displayed on the left hand side and clicked to show the video.


