import numpy as np
import joblib
from extract_landmarks_single import extract_landmarks_single
import cv2

def predice_landmarks(imagen): 
    """Funcion que predice si una imagen pasada por parametro es thumbs up o thumbs down

    Args:
        func (_type_): funcion que devuelve los 21 landmarks,  en formato vector.
        imagen (_type_): imagen a predecir

    Returns:
        _type_: int que será la clase, y devolvera 'Up' si la clase es 1 o 'Down' si la clase es 0
    """

    modload = joblib.load('modelo_entrenado_pipe_SVC.pkl') # Carga del modelo.
    data=extract_landmarks_single(imagen)
    
    if data is None:
        return 'show me your hand'    
    
    pred=modload.predict(data.reshape(1,-1))
    pred_int=np.int_(pred)  
    
    if pred != None:
        if pred_int==1:
            result='Up'
        else:
            result ='Down'  
    else:  
        result= 'FAIL'
    print(result)
    return result
 
 
 
if __name__== '__name__':       
    image=cv2.imread('./train/down87.png')
    predice_landmarks(image)
