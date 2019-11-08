#verificador 3 : calcular la densidad
densidad, masa, volumen=0.0, 0.0, 0.0
#asignacion de valores
masa=int(input("mostrar la mesa:"))
volumen=int(input("mostrar el volumen:"))
#calculo
densidad=masa/volumen
verificador=(densidad==45)
#mostrar valores
print("masa:",masa)
print("volumen:",volumen)
print("densidad:",densidad)
print("densidad==45:",verificador)
