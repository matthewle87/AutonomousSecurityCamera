A program that takes in a video feed and uses AI to detect faces/bodies and begins recording, sending it to a backend server that communicates it to the frontend website.

First demo:

https://github.com/lllyasviel/Fooocus/assets/111463817/37894ea8-cd9a-4b6a-b261-208cc2b656f0

Requirements:
"pip install opencv-python"
"pip install -r requirements.txt"


How to use:
1. cd into downloaded GitHub Folder and run "python backend.py"
2. Run securitycam.py and let the video stream watch for movement and ensure that the working directory is in AutonomousSecurityCamera/FRONTEND/flask_react/public/videos so that videos will be saved in there.
3. cd "FRONTEND/flask_react" and run "npm start". If there are videos present in the current directory, then they will be displayed on the left hand side and clicked to show the video.

Notes:
1. Frontend will be improved to allow for searching and sorting and general aesthetic.
