class Persona:
    
    def __init__(self,nombre):
        self.__nombre = nombre #Este atributo es privado, dolo se puede modificar desde la clase
                                #Si no uso el __ es un atributo publico
    
    def getNombre(self):
        return(self.__nombre)
    
    def setNombre(self,nombre):
        self.__nombre = nombre
        
p1 = Persona("Tobias")
print(p1.getNombre())
p1.__nombre = "Juan"    #Ahora esto no es valido por ser privado
print(p1.getNombre())   #Se ve que no se modifico
p1.setNombre("Roman")
print(p1.getNombre())