#Las variables que se utilizan en el bloque try/except se deben declarar fuera del mismo
#Ya que si hay un error y se declaro ahí la varaible se elimina al no poder procesarlo
try:
    10/0    #No se puede y salta un error
#except:     #Con esto atajo el error, lo cacheo
except Exception as e :
    print("Ocurrió un error",e)

"""
Podria hacer input y try/except con int para que el usuario ingrese un numero y no una palabra
"""

a = int(input("Numerando: "))
b = int (input("Dividendo: "))
res = None
try :
    res = a/b
except ZeroDivisionError as e:
    print("No se puede dividir por 0", e)
except Exception as e:
    print("Ocurrió un error",e)