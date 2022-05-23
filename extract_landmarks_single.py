import mediapipe as mp
from PIL import Image, ImageOps
import cv2
import numpy as np


def extract_landmarks_single(image):
    mp_drawing = mp.solutions.drawing_utils
    mp_hands=mp.solutions.hands
    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.5) as hands:
        key = []

        
        height, width, _= image.shape
        image = cv2.flip(image,1)

        image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

        results=hands.process(image_rgb)
              
        if results.multi_hand_landmarks is not None:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, # image to draw
                    hand_landmarks, # model output
                    mp_hands.HAND_CONNECTIONS)
             
                
               
                
                for data_point in hand_landmarks.landmark:
                    key.append([data_point.x, data_point.y, data_point.z])

              
  


            return np.hstack(np.array(key))

        else:
            return None




