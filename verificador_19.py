#verificador 19: calcular la energia cinematica
energia_cinematica, masa, velocida=0.0, 0.0, 0.0,
#asigancion de valores
masa=int(input("mostrar la masa:"))
velocidad=int(input("mostrar la velocidad"))
#calculo
energia_cinematica=1/2*masa*velocidad**2
verificador=(energia_cinematica<38)
#mostrar valores
print("masa:",masa)
print("velocidad:",velocidad)
print("energia cinematica:",energia_cinematica)
print("energia cinematica<38",verificador)
