import cv2
import numpy as np

video_path = "Livro.mp4"
cap = cv2.VideoCapture(video_path)

lower_HSV = np.array([20, 50, 50])
upper_HSV = np.array([40, 255, 255])

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (500, 500))
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img_hsv, lower_HSV, upper_HSV)

    cv2.imshow("Video Original", frame)

    cv2.imshow("Mascara", mask)

    if cv2.waitKey(10) & 0xFF == ord('q'):
                  #fps
        break

cap.release()
cv2.destroyAllWindows()

#webCam:
#parâmetro 0 no lugar de "cap = cv2.VideoCapture(0)"