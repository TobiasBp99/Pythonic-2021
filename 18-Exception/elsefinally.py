a = int(input("Numerando: "))
b = int (input("Dividendo: "))
res = None
try :
    res = a/b
except ZeroDivisionError as e:
    print("No se puede dividir por 0", e)
except Exception as e:
    print("Ocurrió un error",e)
else :
    print("Todo salió OK")