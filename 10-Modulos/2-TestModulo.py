import ModuoAritmetica as ma    #Importo el archivo y lo puedo usar bajo su alias
                                #No le puedo asignar numeros al archivo porque es un error

from ModuloPersona import Persona as Persona

"""
Si hago
import ModuloPersona
importo todo el archivo pero debo escribir Persona.p1 para hacer uso de la clase

"""

print(ma.sumar(3,4))

p1 = Persona("Tobias" , 21)
print(p1)