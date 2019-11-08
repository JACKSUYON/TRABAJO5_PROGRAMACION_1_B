#verificador 5: calcular el area total de la piramide
area_total_piramide, area_lateral_piramide, area_base_piramide=0.0, 0.0, 0.0
#asignacion de valores
area_lateral_piramide=int(input("mostar el area lateral de la piramide:"))
area_base_piramide=int(input("mostar el area de la base de la piramide:"))
#calculo
area_total_piramide= area_lateral_piramide + area_base_piramide
verificador=(area_total_piramide!=62)
#mostrar valores
print("area lateral de la piramide:",area_lateral_piramide)
print("area de la base de la piramide:",area_base_piramide)
print("area total de la piramide",area_total_piramide)
print("area total de la piramide=!62",verificador)
