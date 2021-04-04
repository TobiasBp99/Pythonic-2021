class MiClase:
    
    var_clase = "Mi variable de clase"
    
    def __init__(self):
        self.var_ins = "Variable instancia"
    
    @staticmethod                   #Decorador que agrega funcionalidad
    def metodo_estatico():          #Se asocia a la clase, no al objeto por eso no recibe a self ni ningun atributo de la instancia
        print("Método estático")
        print(MiClase.var_clase)    #Así accedo a las variables de clase desdde acá por medio del nombre de la clase
        
    @classmethod
    def metodo_clase(cls):          #Por convenciòn se usa con el nombnre de la clase
        print("Metodo de clase :" + str(cls))
        print(cls.var_clase)        #Así accedo a las variables de clase desdde acá por medio del nombre de la clase cls
        
    def metodo_instancia(self):
        print(self.var_ins)
        self.metodo_estatico()  #Desde las instancias puedo acceder a lo estàtico relacionado con la clase
        self.metodo_clase()
        
"""
Lo estàtico solo accedo a lo estatico
Lo de instancia puede acceder a todo ya que la clase para ese entonces ya se encuentra creada
"""


MiClase.metodo_estatico()
MiClase.metodo_clase()

obj = MiClase()
print("+++++++++++++")
obj.metodo_instancia()