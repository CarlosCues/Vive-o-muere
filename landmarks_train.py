from extract_landmarks import extract_landmarks
from os import listdir
import cv2

basepath=[f'train/{imagen}' for imagen in listdir('train') ]

landmarks_train=map(extract_landmarks,basepath[:3])
landmarks_train=list(landmarks_train)
print(landmarks_train)