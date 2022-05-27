from datetime import datetime
import os
import pyautogui as pg

def escribe_fecha(nombre_archivo):
    fecha=datetime.today().strftime('%d-%m-%y')
    with open(nombre_archivo + '.txt','a+') as f:
        filesize = os.path.getsize(nombre_archivo +'.txt')     
        if filesize==0:
            f.write(fecha)
            f.write('\n')        
            return f
        else:
            return f 
        
        
def guardar():
    pg.hotkey('ctrl', 'g')
    pg.hotkey('enter')

          
def check_file(archivo):
    fecha=datetime.today().strftime('%d-%m-%y')
    g=open(archivo.name,'a+') 
    lineas=g.readlines()
    g.close()
 
    for linea in lineas:
        if  fecha != linea[:-1]:
            g=open(archivo.name,'a+') 
            g.write(fecha)
            g.close()                        
        else:
            break

                

