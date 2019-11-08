#boleta 9: calcular tiempo de alcance
#input
distancia=float(input("ingrese distancia:"))
velocidad1=int(input("ingrese velocida1:"))
velocidad2=int(input("ingrese velocidad2:"))

#processing
tiempo_alcance=(distancia)/(velocidad1 - velocidad2)

#verificador
verificador=(tiempo_alcance==90)

#output
print("#########################################")
print("#     BOLETA DE TIEMPO DE ALCANCE       #")
print("#########################################")
print("# datos                                  ")
print("#distancia :   ",distancia)
print("#velocidad 1:   ",velocidad1)
print("#velocidad 2:   ",velocidad2)
print("#tiempo alcance:   ",tiempo_alcance)
print("#########################################")
print("#tiempo de alcance==90:   ",verificador)
