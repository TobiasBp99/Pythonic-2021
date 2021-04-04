class Persona :
    
    def __init__(self,nombre,edad): # Es el constructor. Self es una referencia al objeto
        self.nombre = nombre        #self.atributo son los atributos de la clase, la coincidencia de nombre es por una cuestion de orden
        self.edad = edad
        
persona1 = Persona("Tobias",21)
persona2 = Persona("Tevez", 36)

print(persona1.nombre,persona1.edad)
print(persona2.nombre,persona2.edad)

class Aritmetica:
    
    def __init__(self,op1,op2):
        self.op1 = op1
        self.op2 = op2
    
    def sumar(self):
        return( self.op1 + self.op2 )
    
aritmetica = Aritmetica(2,4)
print(aritmetica.sumar())