from empleado import Empleado

class Gerente(Empleado):
    
    def __init__(self,nombre,sueldo,departamento):
        super().__init__(nombre,sueldo)     #Llamo al constructor de la clase padre
        self.departamento = departamento
        
    
        
    def __str__(self):
        return(super().__str__()+" , Departamento:"+self.departamento)