nota = int(input("Ingrese la calificación:\t"))

if nota < 0 or nota > 10 :
    print("Calificación inválida")
elif nota >= 9:
    print("A")
elif nota >= 8:
    print("B")
elif nota >= 7:
    print("C")
elif nota >= 6:
    print("D")
else:
    print("F")