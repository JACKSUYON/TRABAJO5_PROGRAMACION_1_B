#verificador 11: calcular la potencia
potencia, trabajo1, tiempo=0.0, 0.0, 0.0
#asignacion de valores
trabajo1=int(input("mostrar el trabajo:"))
tiempo=int(input("mostrar el tiempo:"))
#calculo
potencia=trabajo1/tiempo
verificador=(potencia>=17)
#mostrar valores
print("trabajo1:",trabajo1)
print("tiempo:",tiempo)
print("potencia:",potencia)
print("potencia>=17",verificador)
