#verificador 17: calcular tiempo de alcance
tiempo_alcance, distancia, velocidad_1, velocidad2=0.0, 0.0, 0.0, 0.0
#asigancion de valores
distancia=int(input("mostrar distancia:"))
velocidad1=int(input("mostrar velocida1:"))
velocidad2=int(input("mostara velocidad2:"))
#calculo
tiempo_alcance=(distancia)/(velocidad1 - velocidad2)
verificador=(tiempo_alcance==90)
#mostrar valores
print("distancia :",distancia)
print("velocidad 1:",velocidad1)
print("velocidad 2:",velocidad2)
print("tiempo alcance:",tiempo_alcance)
print("tiempo de alcance==90",verificador)
