#verificador 6: calcular el volumen de la piramide
volumen_piramide, area_base_de_la_piramide, altura=0.0, 0.0, 0.0
#asignacion de valores
area_base_de_la_piramide=int(input("mostrar el area de la base:"))
altura=int(input("mostrar la altura:"))
#calculo
volumen_piramide=(area_base_de_la_piramide*altura)/3
verificador=(volumen_piramide>36)
#mostrar valores
print("area de la base de la piramide:",area_base_de_la_piramide)
print("altura:",altura)
print("volumen de la piramide:",volumen_piramide)
print("volumen de la piramide>36",verificador)
