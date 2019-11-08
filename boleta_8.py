#boleta 8: calcular el tiempo de enuentro
#input
distancia=float(input("ingrese distancia:"))
velocidad1=int(input("ingrese velocidad:"))
velocidad2=int(input("ingrese velocidad 2"))
#processing
tiempo_encuentro=(distancia)/(velocidad1 + velocidad2)

#verificador
verificador=(tiempo_encuentro<=30)

#output
print("########################################################")
print("#     BOLETA DE LA FORMULA DE TIEMPO DE ENCUENTRO      #")
print("########################################################")
print("#  datos")
print("#distancia:   ",distancia                                )
print("#velocidad:   ",velocidad1                               )
print("#velocidad:    ",velocidad2                              )
print("#tiempo de encuentro:   ",tiempo_encuentro               )
print("########################################################")
print("#tiempo de encuentro<=30",verificador)
