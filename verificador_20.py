#verificador 20: calcular la presion hidrostatica
presion_hidrostatica, densidad, gravedad, altura=0.0, 0.0, 0.0, 0.0
#asignacion de valores
densidad=int(input("mostrar densidad:"))
gravedad=int(input("mostrar la gravedad:"))
altura=int(input("mostrar la altura:"))
#calculo
presion_hidrostatica=densidad*gravedad*altura
verificador=(presion_hidrostatica>=32)
#mostrar valores
print("densidad0:",densidad)
print("gravedad0:",gravedad)
print("altura0:",altura)
print("presion hidrostatica:",presion_hidrostatica)
print("presion hidrostatica>=32",verificador)
