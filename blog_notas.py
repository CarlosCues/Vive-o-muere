
import subprocess 
from datetime import datetime
import os

class Notepad:

    def __init__(self,programa="notepad.exe",archivo="Mynotes"):
        self.programa=programa
        self.archivo= archivo
        self.process=None
    
    def abrir(self):      
        if self.process == None:
            print("Öpen notepad")            
            self.process = subprocess.Popen([self.programa,self.archivo])            
        else:
            print("Älready opened")
    
                 
  
        
        
    def cerrar(self): 
        if self.process:
            self.process.terminate()
            self.process = None
            return
        else:
            print("¨Not opened yet")
    

def archivo():            
        fecha=datetime.today().strftime('%d-%m-%y')
        print('FECCHAAAA',type(fecha))
        with open('mynotes.txt','a+') as f:
            lineas = f.readlines()
            print('lineasss',type(lineas))
            if len(lineas)==0:
                print('lineasss',len(lineas))
                f.write(fecha)                
            else:
                for linea in lineas:
                    if  fecha != linea:
                        f.write(fecha)
                        
                    else:
                        break 