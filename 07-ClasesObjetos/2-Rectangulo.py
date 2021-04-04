class Rectangulo :
    
    def __init__(self,b,h):
        self.b = b
        self.h = h
        
    def getArea(self):
        return(self.b*self.h)
    
base = int(input("Ingrese la medida de la base [cm]:\t"))
heigth = int(input("Ingrese la medida de la altura [cm]:\t"))

rectangulo = Rectangulo(base,heigth)
print("El rectangulo tiene un area de : ",rectangulo.getArea(),"cm^2")