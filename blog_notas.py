import subprocess 

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
            print("Not opened yet")
    

