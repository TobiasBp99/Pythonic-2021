from abc import ABC,abstractmethod

class Figura(ABC):  #Ahora mi clase no hereda de la clase Object
                    #SIno de la clase Abstract Based CLass
    
    def __init__(self,ancho,alto):
        self.ancho = ancho
        self.alto = alto
        
    """
    Esto es un decorador que me indica que el método es abstracto
    Esto me obliga a definir el método en las clases hijas, sino las clases serán abstractas también
    """    
    @abstractmethod
    def area (self):    #Es un mètodo comùn a la clase pero cada hijo lo trata de una forma distinta
        pass
        
    
        
    def __str__(self):
        return("Ancho: " + str(self.ancho) + "\tAlto: " + str(self.alto))