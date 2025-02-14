import cv2
import mediapipe as mp
import time
import os
from datetime import datetime


# Initialize Pose Detection
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for AVI format
out = cv2.VideoWriter('pose_detection.avi', fourcc, 20.0, (640, 480))  # Save at 20 FPS

# Alarm settings
alarm_triggered = False  # Start with alarm OFF
out_of_bed = False
start_time = 0
delay_threshold = 30  # Require 10 seconds of standing to stop alarm
alarm_time = "09:30"  # Set alarm to ring at 9:30 AM

# Function to detect if standing
def detect_standing(landmarks):
    if landmarks:
        shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
        hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y
        knee = landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y
        return hip > shoulder and knee > hip  # Standing means hips above knees
    return False

# Wait until 9:30 AM before triggering alarm

while True:
    now = datetime.now().strftime("%H:%M")  # Get current time in HH:MM format
    if now == alarm_time:
        break  # Exit loop when it's 9:30 AM
    print(f"Waiting for alarm time... Current time: {now}")
    time.sleep(5)  # Check the time every 30 seconds to save CPU usage



# Start alarm in repeat mode
alarm_triggered = True
print("Alarm Started!")
os.system('start wmplayer /play /repeat "C:\\Users\\arask\\source\\repos\\workspace\\Melon-Alarm\\mix_4m44s (audio-joiner.com) (1).mp3"')

# Keep alarm ringing until user stands up for 10 seconds
while alarm_triggered:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)

    if results.pose_landmarks:
        standing = detect_standing(results.pose_landmarks.landmark)
        print(f'Standing: {standing} | Out of Bed: {out_of_bed} | time = {datetime.now().strftime("%H:%M:%S")}')
        if standing:
            print(f'Standing: {standing} | Out of Bed: {out_of_bed} | time = {datetime.now().strftime("%H:%M:%S")}')

            if not out_of_bed:
                print(f'Standing: {standing} | Out of Bed: {out_of_bed} | time = {datetime.now().strftime("%H:%M:%S")}')

                out_of_bed = True
                start_time = time.time()  # Start timing standing duration
                print(f'Standing: {standing} | Out of Bed: {out_of_bed} | time = {datetime.now().strftime("%H:%M:%S")} | start_time = {start_time}')    

            elif time.time() - start_time >= delay_threshold:
                alarm_triggered = False
                print("Alarm Stopped!")
                
                # Close Windows Media Player
                os.system('taskkill /IM wmplayer.exe /F')
                break
        else:
            out_of_bed = False  # Reset if user sits back down
            print(f'Standing: {standing} | Out of Bed: {out_of_bed} | time = {datetime.now().strftime("%H:%M:%S")}')
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)



    cv2.imshow("Pose Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # Press q to make the torture stop
        break

cap.release()

out.release()
cv2.destroyAllWindows()

cv2.destroyAllWindows()

