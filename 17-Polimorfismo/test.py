from empleado import Empleado
from gerente import Gerente

def imprimir_detalles(tipo_padre):
    print(tipo_padre)
    
empleado = Empleado("Juan",1000)
imprimir_detalles(empleado) #Obviamente llamo al str de la clase empleado

empleado = Gerente("Karla",2000.00,"Flow & Level")  #Ahora apunta a un objeto de la clase tipo hija
imprimir_detalles(empleado)


