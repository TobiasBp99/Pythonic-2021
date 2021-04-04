from Figura import Figura
from Color import Color

class Cuadrado(Figura,Color):
    
    def __init__(self,lado,color):
        #Ya no puedo usar super porque los padres
        #tienen distinta prioridad pero siempre figura sera donde busque
        
        Figura.__init__(self,lado,lado) #Debo pasar self porque desde la clase padre toco una referencia que es de un hijo
        Color.__init__(self,color)
        
    def area(self):
        return (self.ancho*self.alto)
    
    def __str__(self):
        string_f = Figura.__str__(self)
        string_c = Color.__str__(self)
        return(string_f + '\n' + string_c + '\n' +"<----x---->")
        
c = Cuadrado(5,"Amarillo")
print(c.area())

#Method resolution order
#Muestra el orden en que se ejecutan las clases
print(Cuadrado.mro())

print(c)
