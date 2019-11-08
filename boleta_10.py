#boleta 10: calcular la presion hidrostatica
#input
densidad=float(input("ingrese la densidad:"))
gravedad=int(input("ingrese la gravedad:"))
altura=float(input("ingrese la altura:"))

#processing
presion_hidrostatica=densidad*gravedad*altura

#verificador
verificador=(presion_hidrostatica>=32)
#output
print("#########################################################")
print("#    BOLETA DE LA FORMULA DE LA PRESION HIDROSTATICA    #")
print("#########################################################")
print("#    datos")
print("#densidad0:   ",densidad)
print("#gravedad0:   ",gravedad)
print("#altura0:   ",altura)
print("#presion hidrostatica:   ",presion_hidrostatica)
print("##########################################################")
print("#presion hidrostatica>=32:   ",verificador)
