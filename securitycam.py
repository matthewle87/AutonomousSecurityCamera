import cv2
import time
import datetime
import requests

cap = cv2.VideoCapture(0)

#classifies the body and face in the video stream
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")

detection = False
stopped_time = None
timer_started = False
running = True
after_detection_seconds = 5
BASE = "http://127.0.0.1:5000/"

frame_size = (int(cap.get(3)), int(cap.get(4)))
#videos must be h.264 encoding
fourcc = cv2.VideoWriter_fourcc(*"X264")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: No camera detected.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #detects faces and bodies
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodies = body_cascade.detectMultiScale(gray, 1.3, 5)

    #if faces or bodies are detected, begin recording
    if len(faces) + len(bodies) > 0:
        if detection:
            timer_started = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            times = current_time.split("-")
            #sends the information to the backend
            requests.put(BASE + "put", {"name": current_time + ".mp4", "year": times[2], 'month': times[1], 'day': times[0]}) 
            out = cv2.VideoWriter(
                f"{current_time}.mp4", fourcc, 30.0, frame_size)
            print("Started Recording!")
    elif detection:
        if timer_started:
            if time.time() - stopped_time >= after_detection_seconds:
                detection = False
                timer_started = False
                out.release()
                print('Stop Recording!')
        else:
            timer_started = True
            stopped_time = time.time()

    if detection:
        out.write(frame)

    #draws a box around the face detected
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        if detection:
            print('Stop Recording!')
            out.release()
        break

cap.release()
cv2.destroyAllWindows()