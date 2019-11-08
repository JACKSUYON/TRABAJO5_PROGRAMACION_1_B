#verificador 16: calcular el tiempo de enuentro
tiempo_encuentro, distancia, velocidad1, velocidad2=0.0, 0.0, 0.0, 0.0
#asigancion de valores
distancia=int(input("mostrar distanccia:"))
velocidad1=int(input("mostrar velocidad:"))
velocidad2=int(input("mostrar velocidad 2"))
#calculo
tiempo_encuentro=(distancia)/(velocidad1 + velocidad2)
verificador=(tiempo_encuentro<=30)
#mostrar valores
print("distancia:",distancia)
print("velocidad:",velocidad1)
print("velocidad:",velocidad2)
print("tiempo de encuentro:",tiempo_encuentro)
print("tiempo de encuentro<=30",verificador)
