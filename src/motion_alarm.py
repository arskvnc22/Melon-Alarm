import cv2
import numpy as np
import time
import os # For playing alarm sound
import yt_dlp
# Open webcam
cap = cv2.VideoCapture(0)


# Read first frame
ret, frame1 = cap.read()
frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
frame1 = cv2.GaussianBlur(frame1, (21, 21), 0)

alarm_triggered = False
alarm_time = 0
alarm_duration = 10  # Alarm must sound for at least 10 seconds

while True:
    ret, frame2 = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Compute difference
    diff = cv2.absdiff(frame1, gray)
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    
    # Find movement contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:  # If movement is detected
        if not alarm_triggered:
            alarm_triggered = True
            alarm_time = time.time()
            print("ALARM TRIGGERED!")
            os.system('start "" "C:\\Users\\arask\\source\\repos\\workspace\\Melon-Alarm\\kazakhstan ugrazaj nambambierofke.mp3"')

    # Stop alarm after a delay
    if alarm_triggered and time.time() - alarm_time >= alarm_duration:
        alarm_triggered = False
        print("ALARM STOPPED!")

    cv2.imshow("Webcam Feed", frame2)
    frame1 = gray  # Update reference frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
