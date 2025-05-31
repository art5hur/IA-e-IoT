import cv2
from matplotlib import pyplot as plt
import numpy as np

video_path = "Livro.mp4"
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (500, 500))
    img_canny = cv2.Canny(frame, 350,350)

    cv2.imshow("Video Original", frame)
    cv2.imshow("Mascara", img_canny)

     # Pressione 'q' para sair
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



