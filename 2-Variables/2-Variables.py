x = 5
print("X = ",x)
y = 3
print("Y = ",y)
z = x+y 
print("Z = X+Y ",z)

w = z
print("W = Z = ",w)

z +=1
w-=1 #Esto increíblemente utiliza ell mismo lugar de memoria, pero luego los diferencia
#Cada objeto igual en Python usa el mismo espacio de memoria para optimizar lugar, sin embargo el modificar uno no altera el contenido de otro.
# a = 1 
# b = 1 
# Ambos ocupan el mismo lugar en la memoria
print(z,w)