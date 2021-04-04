"""
Acá se preuban todas las clases
"""
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

c = Cuadrado(5,"Amarillo")
print(c.area())

#Method resolution order
#Muestra el orden en que se ejecutan las clases
print(Cuadrado.mro())

print(c)

r = Rectangulo(5,7,"Amarillo pollito")
print(r.area())