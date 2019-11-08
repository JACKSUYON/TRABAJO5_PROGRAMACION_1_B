#verificador 10: calcular la energia potencial gravitatoria
eneria_ptencial_gravitatoria, masa1, gravedad, altura1=0.0, 0.0, 0.0, 0.0
#asignacion valores
masa=int(input("mostrar masa:"))
gravedad=int(input("mostrar gravedad:"))
altura=int(input("mostrar altura:"))
#calculo
energia_potencial_gravitatoria=(masa*gravedad*altura)
verificador=(eneria_ptencial_gravitatoria==64)
#mostrar valores
print("masa:",masa)
print("gravedad:",gravedad)
print("altura:",altura)
print("energia ptencial gravitatoria:",energia_potencial_gravitatoria)
print("energia potencial gravitatoria==64:",verificador)
