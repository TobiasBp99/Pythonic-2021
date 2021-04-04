d_resistencias = {"1k":1000 , "2k": 2000 , "3k3": 3300}

print("El diccionario tiene ",len(d_resistencias),"elementos")

print(d_resistencias["3k3"])    #se indexa con las keys
print(d_resistencias.get("1k")) #asi tambien puedo obtener los value

for key in d_resistencias:      #itero sobre las key y luego puedo procesar los value
    print(key,d_resistencias[key],sep=':')
    
d_resistencias["4k7"] = 4700
d_resistencias["1k"] = "1000 Ohm"
"""
Así puedo modificar un value o haer un append
"""
print(d_resistencias)
d_resistencias.pop("3k3")
print(d_resistencias)