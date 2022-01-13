import cv2
import mediapipe as mp
import glob

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

training_data = []

# For static images:
IMAGE_FILES = []
index = 0

data_file = open("training.dat", "w")

with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
  for idx, file in enumerate(glob.glob('train_hands/*.jpg')):
    # Convert the BGR image to RGB before processing.
    image = cv2.imread(file)
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    height, width, _ = image.shape

    if not results.multi_hand_landmarks:
        continue

    for hand in results.multi_hand_landmarks:
        xmin = 1
        ymin = 1
        xmax = 0
        ymax = 0
        for landmark in hand.landmark:
            if xmin > landmark.x:
                xmin = landmark.x
            if ymin > landmark.y:
                ymin = landmark.y
            if xmax < landmark.x:
                xmax = landmark.x
            if ymax < landmark.y:
                ymax = landmark.y

        ymin = ymin * height
        xmin = xmin * width
        ymax = ymax * height
        xmax = xmax * height

        if ymin < 0:
            ymin = 0
        if xmin < 0:
            xmin = 0
        if ymax > height:
            ymax = height
        if xmax > width:
            xmax = width
        # print(xmin,ymin,xmax,ymax)
        # image = cv2.rectangle(image,(int(xmin*width),int(ymin*height)),(int(xmax*width),int(ymax*height)),(0,255,0),3)
            # training_data.append([file, 'Palm', box.xmin, box.ymin, None, None, box.xmin + box.width, box.ymin + box.height])
        f.write("{} 1 {} {} {}".format(file, xmin, ymin, xmax-xmin, ymax-ymin))
    # cv2.imwrite('test.jpg', image)
