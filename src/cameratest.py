print("Hello from cameratest.py")

import cv2

# Open wbcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() # ret = bool wether frame is read or not, frame = image, if ret = true numpy array
    if not ret:
        break

    cv2.imshow("Webcam Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # 0xFF is a mask, ord('q') returns the unicode of 'q'
        break

cap.release()#release device
cv2.destroyAllWindows()
print("Goodbye from cameratest.py")