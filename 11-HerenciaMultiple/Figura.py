class Figura:
    
    def __init__(self,ancho,alto):
        self.ancho = ancho
        self.alto = alto
        
    def __str__(self):
        return("Ancho: " + str(self.ancho) + "\tAlto: " + str(self.alto))