class Orden:
    
    contador_ordenes = 0
    
    def __init__(self,l_productos):
        Orden.contador_ordenes += 1               #Establece el numero de ordenes
        self.__id_orden = Orden.contador_ordenes  #Genere el ID de cada orden a medida que se vayan cargando
        self.__prdouctos = l_productos              #Esto hace que productos se referencia al lugar de memoria de l_productos
        
    def __str__(self):
        producto_str = ""
        for p in self.__prdouctos:
            #producto_str += p.__str__() + '|'  
            producto_str += str(p) + '\n'        #Cualquier forma es equivalente ya que el casteo es un llamado al metodo str
        return("ID orden:"+str(self.__id_orden)+"\n"+producto_str)
    
    def agregar_producto(self,producto):
        """
        Me permite agregar un producto a la lsita sin tenet que editarla en varias lineas desde el main
        """
        self.__prdouctos.append(producto)
        
    def calcular_total(self):
        total = 0
        for p in self.__prdouctos:
            total += p.get_precio()
        return (total)