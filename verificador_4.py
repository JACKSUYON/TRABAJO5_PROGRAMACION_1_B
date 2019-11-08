#verificador 4: calcular el area lateral de un cono
area_lateral_cono, pi, radio, generatriz=0.0, 0.0, 0.0, 0.0
#asignacion de valores
pi=3.1416
radio=int(input("mostrar el radio:"))
generatriz=int(input("mostrar generatriz:"))
#calculo
area_lateral_cono=(pi*radio*generatriz)
verificador=(area_lateral_cono<=65)
#mostrar valores
print("pi:",pi)
print("radio:",radio)
print("generatriz:",generatriz)
print("area lateral del cono:",area_lateral_cono)
print("area lateral del cono<=65:",verificador)
