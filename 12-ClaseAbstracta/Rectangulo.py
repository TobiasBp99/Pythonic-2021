from Figura import Figura
from Color import Color

class Rectangulo(Figura,Color):
    
    def __init__(self,ancho,alto,color):
        self.ancho = ancho
        self.alto = alto
        self.color = color
        
    def area (self):
        return(self.ancho*self.alto)