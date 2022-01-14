import cv2
import math
import numpy as np

img = cv2.imread('FromEsp32/picture19.jpg')
img = cv2.flip(img, 0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.array([
  [1, 0, -1],
  [2, 0, -2],
  [1, 0, -1]
])

r = cv2.filter2D(gray, -1, kernel)
_,thresh1 = cv2.threshold(r,127,255,cv2.THRESH_BINARY)

kernel = np.array([
  [-1, 0, 1],
  [-2, 0, 2],
  [-1, 0, 1]
])

r2 = cv2.filter2D(gray, -1, kernel)
_,thresh2 = cv2.threshold(r2,127,255,cv2.THRESH_BINARY)

img = cv2.bitwise_or(thresh1, thresh2)

kernel = np.array([
  [1, 2, 1],
  [0, 0, 0],
  [-1, -2, -1]
])

r3 = cv2.filter2D(gray, -1, kernel)
_,thresh3 = cv2.threshold(r3,127,255,cv2.THRESH_BINARY)

img = cv2.bitwise_or(img, thresh3)

kernel = np.array([
  [-1, -2, -1],
  [0, 0, 0],
  [1, 2, 1]
])

r4 = cv2.filter2D(gray, -1, kernel)
_,thresh4 = cv2.threshold(r4,127,255,cv2.THRESH_BINARY)

img = cv2.bitwise_or(img, thresh4)

annotated = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

# for column in range(w):
#     longest = 0
#     current = 0
#     for row in range(h):
#         if r[row][column] > 100:
#             current += 1
#         else:
#             if current > longest:
#                 longest = current
#                 current = 0
#
#     if longest > 8:
#         cv2.line(annotated,(column,0),(column,h),(255,0,0),1)

cv2.imshow('test', annotated)
cv2.waitKey(0)
