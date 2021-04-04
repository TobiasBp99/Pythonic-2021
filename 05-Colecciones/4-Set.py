"""
No mantiene el orden    -> no se puede indexar
                        -> Cada vez que imprimo veo orden diferente
Los elementos se almacenan una sola vez

Creo que desde Python 3.algo ya mantiene el orden y siempre se imprime lo mismo
"""

planetas = {"Marte","Jupiter","Venus"}

print(planetas)
print(planetas)

print("El set tiene",len(planetas),"elementos")

planetas.add("Tierra")
print(planetas)
#No puedo repetir un elemento
planetas.add("Tierra")
print(planetas)

planetas.discard("Venus")
print(planetas)