from orden import Orden
from producto import Producto

p1 = Producto("Banana",100)
p2 = Producto("melon",150.50)

l_productos = [p1,p2]

o1 = Orden(l_productos)

print(o1)

p3 = Producto("Manzana",75.25)
l_productos.append(p3)

print(o1)   #Recordar que se trabaja con punteros y està referenciado
            #Por lo tanto si modifico algo se modificara en tdos lados

new_pro = Producto("Tomate",50)
o1.agregar_producto(new_pro)
print(o1)

p4 = Producto("Papa",300)
p5 = Producto("Durazno",170)

l2 = [p4,p5]
o2 = Orden(l2)
print(o2)   #Vemos que el ID orden funciona OK

print(o2.calcular_total())