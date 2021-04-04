for letra in "Hola":
    print(letra)
#Un for puede funcionar como un while pero 
# tiene la capacidad de iterar sobre una coleccion

for letra in "Holanda":
    if letra == 'a':
        print(letra)
"""
En este caso busco un elemento dentro de la coleccion
"""
for letra in "Holanda":
    if letra == 'a':
        print(letra)
        break
"""
El break rompe totalmente con la cadena
"""

for i in range(6): #Esta funcion me da una lista de 0 a 5
    if i%2 == 0:
        continue
    else:           #No es necesario utilizar el else
        print (i) 
"""
El continue saltea esa iteracion y vuelve al origen del bucle
"""