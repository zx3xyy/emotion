import cv2
import numpy as np
from matplotlib import pyplot as plt
cv2.destroyAllWindows()
face_cascade = cv2.CascadeClassifier('/home/mark/work/emotion/face_extraction/haarcascade_frontalcatface.xml')
img = cv2.imread('images/6.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
print faces
plt.imshow(gray)
plt.show()
