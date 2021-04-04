class Persona:      #Todas las clases por defecto heredan de la clase objeto
    
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):  #Es lo que invoca el print, asì lo modifico al asignado por defecto
        return ("Nombre: " + self.nombre + "\tEdad: " + str(self.edad))
        
class Empleado(Persona):    #Heredo de la clase persona
    
    def __init__(self,nombre,edad,sueldo):  #Si construyo un empleado como heredo de persona necesito sus atributos
        super().__init__(nombre,edad)       #Super invoca los métodos de la clase padre
        self.sueldo = sueldo
    
    def __str__(self):
        return( super().__str__() + "\tSueldo: " + str(self.sueldo))

p1 = Persona("Tobias", 21)
print(p1)
emp = Empleado("TObias",21,1000)
print(emp)