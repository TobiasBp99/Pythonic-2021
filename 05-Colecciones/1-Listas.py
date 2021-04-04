nombres = [ "Florencia" , "Claudia", "Ricardo" , "Tobias"] #Lista de cadenas

index = 0
print("nombres[] almacena",len(nombres),"elementos",sep=' ')
for nombre in nombres:
    print(index,nombre,sep=' ')
    print(nombres[index]) #Asi los puedo indexar y obtener el contenido
    index +=1
"""
Itero sonre la lista y veo como se index los elementos
"""

start = 1
end = 4
print(nombres[start:end]) #Hago slicing de una lista. El slice arrranca en el inicial y otorga final - inicial elementos
new_nombres = nombres[start:end] #Copia una lista en otra lista nueva
print(new_nombres)
new_names = new_nombres #Copia la lista pero funciona como un puntero en C. Si modifico alguna estoy modificando ambos porque es una referencia
new_names[0] = "Roman"
print(nombres,new_names,new_nombres) #En el print veo que ambas new se modifican -> Trabaja como puntero

    