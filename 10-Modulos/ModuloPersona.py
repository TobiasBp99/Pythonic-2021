class Persona:
    
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
        
    def __str__(self):
        return( self.__nombre +"\t"+ str(self.__edad))