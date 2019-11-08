#verificador 2 :calcular el numero de electrones
numero_de_electrones, numero_de_protones, carga=0.0, 0.0, 0.0
#asignacion de valores
numero_de_protones=int(input("mostrar el numero de protones:"))
carga=int(input("mostrar la carga:"))
#calculo
numero_de_electrones=(numero_de_protones + carga)
verificador=(numero_de_electrones>47)
#mostrar valores
print("numero de protones:",numero_de_protones)
print("carga",carga)
print("numero de elctrones",numero_de_electrones)
print("el numero de elctrones>47:",verificador)
