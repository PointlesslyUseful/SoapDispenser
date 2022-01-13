import cv2
import math
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('HaarTrain/train_hands/picture281.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.array([
  [1, 0, -1],
  [2, 0, -2],
  [1, 0, -1]
])

r = cv2.filter2D(gray, -1, kernel)

h,w = r.shape

annotated = gray = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

for column in range(w):
    longest = 0
    current = 0
    for row in range(h):
        if r[row][column] > 100:
            current += 1
        else:
            if current > longest:
                longest = current
                current = 0

    if current > 10:


cv2.imwrite('test.jpg', r)
