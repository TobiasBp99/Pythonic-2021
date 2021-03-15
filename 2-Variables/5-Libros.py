print("Proporcione los datos del siguiente libro")
nombre = input("Ingrese el nombre:\t")
id =  int(input("Ingrese el ID:\t"))
precio = float(input("Ingrese el precio:\t"))
envio_gratuito = input("Envío gratuito(true/false):\t")

if envio_gratuito == "true":
    envio_gratuito = True
else:
    envio_gratuito = False