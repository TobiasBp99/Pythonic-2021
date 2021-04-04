#Son atributos asociados a la clase y no a los objetos instanciados

#Todos los objetos acceden al valor de la clase

#Si modifico el atributo desde un objeto ese atributo se crearà asociado con el objeto que lo modifico y sòlo lo podré leer desde dicho objeto

class MiClase:
    var_clase = "Variable de clase" #Variable de clase
    
    def __init__(self,nombre):
        self.nombre = nombre        #Variable de instancia
        

print(MiClase.var_clase)    #No necesito instanciar la clase para acceder a la variable

obj1 = MiClase("Tobias")
print(obj1.nombre,obj1.var_clase)   #Todos los objetos tendrán la misma var_clase

obj2 = MiClase("DaniStone")
print(obj2.nombre,obj2.var_clase)

MiClase.var_clase = "La modifique para tuti"
print(obj1.nombre,obj1.var_clase)
print(obj2.nombre,obj2.var_clase)

obj1.var_clase = "Modifico solo en OBJ1"
obj3 = MiClase("LioMessi")                  #Creo un nuevo objeto

print(obj1.nombre,obj1.var_clase)           #Veo que var_clase se asocio con la instancia
print(obj2.nombre,obj2.var_clase)           #Y acá no ocurrió nada
print(obj3.nombre,obj3.var_clase)           #Y acá no ocurrió nada

MiClase.var_clase = "Otra vez cambio"       #Ahorá veo que solo se modifica donde la variable de clase no se ha asociado a la instancia
print(obj1.nombre,obj1.var_clase)
print(obj2.nombre,obj2.var_clase)
print(obj3.nombre,obj3.var_clase)
