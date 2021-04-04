"""
Contiene la definicion de la clase Producto
"""

class Producto:
    contador_producto = 0   #Variable de clase, la debo modificar desde la CLASE
    
    def __init__(self,nombre,precio):
        Producto.contador_producto +=1  #Incremento en 1 la variable de la clase
        self.__id_prodcuto = Producto.contador_producto #Atributoo privado -> ID = Numero de producto
        self.__nombre = nombre                          #Atributoo privado
        self.__precio = precio                          #Atributoo privado
        
    def get_precio(self):
        return(self.__precio)
    
    def __str__(self):
        return("ID producto:"+str(self.__id_prodcuto)+"\tNombre:"+self.__nombre+"\tPrecio:"+str(self.__precio))
            