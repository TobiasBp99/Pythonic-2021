class Persona:
    
    def __init__(self , nombre , ape_pat , ape_mat ):
        self.nombre = nombre        #publico
        self._ape_pat = ape_pat     #Protegido se usa para indicar que no se deberia modificar desde fuera de la clase
        self.__ape_mat = ape_mat    #Privado solo se modifica por medio de metodos
        
    def __metodoPrivado(self):      #Solo puede ser accedido dentro de la clase
        print(self.nombre)
        print(self._ape_pat)
        print(self.__ape_mat)
        
    def metodoPublico(self):        
        self.__metodoPrivado()
        
p1 = Persona("Tobias" , "Bavasso" , "Piizzi")

#print(p1.nombre,p1._ape_pat,p1.__ape_mat)   #Al materno no puedo acceder desde aca

print(p1.nombre,p1._ape_pat)
#p1.__metodoPrivado()                        #Desde acá no puedo acceder
p1.metodoPublico()                          #Debo utilizar un metodo publico para tocar el privado