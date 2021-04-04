from numeros_identicos_exception import NumerosIdenticosException

res = None  #Las variables que se siguen usando fuera del bloque deben ser creadas fuera, ya que al salir del mismo, se eliminan

try:    #Acá hago todo lo que puede generar un error
    a = int(input("Numerador:"))
    b = int(input("Denominador:"))
    if a == b:
        raise NumerosIdenticosException("Números iguales")  #Esto va al constructor de la clase que cree
    res = a/b
except ZeroDivisionError as e:  #El
    print("No se puede dividir por 0", e)
except TypeError as e:
    print("Formato inválido",e)
except NumerosIdenticosException as e:
    print("Los valores son iguales",e)
except Exception as e:
    print("Ocurrió un error",e)