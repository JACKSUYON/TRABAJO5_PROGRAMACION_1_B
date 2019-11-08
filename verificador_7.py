#verificador 7: clacular el area lateral del cilindro
area_lateral_cilindro, pi, radio1, generatriz1=0.0, 0.0, 0.0, 0.0
#asignacion de valores
pi=3.1416
radio1=int(input("mostrar el radio:"))
generatriz1=int(input("mostrar la generatriz:"))
#calculo
area_lateral_cilindro=(2*pi*radio1*generatriz1)
verificador=(area_lateral_cilindro>=29)
#mortrar valores
print("pi:",pi)
print("radio1:",radio1)
print("generatriz1:",generatriz1)
print("area latera del cilindro:",area_lateral_cilindro)
print("area lateral del cilindro>=29",verificador)
