import cv2
import mediapipe as mp
from blog_notas import Notepad
from file import escribe_fecha,check_file,guardar
from predice_landmarks import predice_landmarks



mp_drawing= mp.solutions.drawing_utils
mp_hands= mp.solutions.hands

cap=cv2.VideoCapture(0)
n=Notepad()
name='mynotes'


while True:
    ret, frame = cap.read()
    data=predice_landmarks(frame)
    print(data)

    if data =='Up':  
        n.abrir()
        escribe_fecha(name)
        check_file(escribe_fecha(name))

    if data=='Down':
        guardar()
        n.cerrar()       
    
    ###imprimier texto en imagen
    
    font = cv2.FONT_HERSHEY_TRIPLEX
    position=(50,50)
    fontsale=1
    color=(0,0,0)
    thickness=3
    label= data
    frame= cv2.putText(frame,label,position,font,fontsale,color,thickness,cv2.LINE_AA)

    cv2.imshow('Signals',frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows