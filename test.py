import cv2
import math
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('HaarTrain/train_hands/picture292.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.array([
  [1, 0, -1],
  [2, 0, -2],
  [1, 0, -1]
])

r = cv2.filter2D(gray, -1, kernel)



cv2.imwrite('test.jpg', r)
