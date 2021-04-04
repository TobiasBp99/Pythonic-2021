#Las tuplas son elemetos inmutables
frutas = ("Naranja", "banana", "Manzana")
#Se inicializa con ()
print(frutas)

print("La tupla tiene", len(frutas), "elementos")

print(frutas[0:2])  #Puedo hacer slicing

"""
Los valores no pueden ser modificados asi que
para cambiar una tupla o debo sobreescribirla 
o la debo convertir a lista ppara despues 
pasar a tupla otra vez

Esto mismo aplica para hacer append o remove
"""
frutas = ("Naranjita", "banana", "Manzana")
print(frutas)
l_frutas = list(frutas)
l_frutas[0] = "Naranjon"
t_frutas = tuple(l_frutas)
print(t_frutas)


#Se itera igual que una lista
index = 0
for fruta in frutas:
    print(index, fruta)
    index +=1