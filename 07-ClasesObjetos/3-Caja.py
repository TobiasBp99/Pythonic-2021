class Caja:
    
    def __init__(self,w,h,l):
        self.w = w
        self.h = h
        self.l = l
        
    def getVolume(self):
        return(self.w*self.h*self.l)
    
width = int(input("Ingrese el ancho:\t"))
heigth = int(input("Ingrese el alto:\t"))
large = int(input("Ingrese el largo:\t"))

c = Caja(width,heigth,large)

print("Volumen : ",c.getVolume())