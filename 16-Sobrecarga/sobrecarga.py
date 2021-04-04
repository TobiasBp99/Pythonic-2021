class Persona:
    
    def __init__(self,nombre):
        self.__nombre = nombre
        
    def __add__(self,otro): #Estoy sobreescribiendo y sobrecargado un mètodo de la clase object
        return(self.__nombre +' '+otro.__nombre)
    """
    Se dice que lo sobreescribo porque hago uso de un metodo que no tenìa
    Y sobrecargo porque le puedo dar la funcionalidad que yo quiera
    """
    
p1 = Persona("Tobias")
p2 = Persona("Roman")

print(p1+p2)