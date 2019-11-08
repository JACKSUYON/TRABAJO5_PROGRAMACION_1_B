#verificador 12: calcular la fuerza
fuerza, masa, aceleracion=0.0, 0.0, 0.0
#asigancion de valores
masa=int(input("mostrar masa:"))
aceleracion=int(input("mostrar la aceleracion:"))
#calculo
fuerza=(masa * aceleracion)
verificador=(fuerza!=55)
#mostrar valores
print("masa:",masa)
print("aceleracion:",aceleracion)
print("fuerza:",fuerza)
print("fuerza!=55:",verificador)
