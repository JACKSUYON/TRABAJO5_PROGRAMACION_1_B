#boleta 5: calcular el area total de la piramide
#input
area_lateral_piramide=int(input("ingrese el area lateral de la piramide:"))
area_base_piramide=int(input("ingrese el area de la base de la piramide:"))

#processing
area_total_piramide= area_lateral_piramide + area_base_piramide

#verificador
verificador=(area_total_piramide!=62)

#output
print("#################################################")
print("#        BOLETA DEL AREA TOTAL DE LA PIRAMIDE    #")
print("#################################################")
print("# datos  "                                        )
print("#area lateral de la piramide:    ",area_lateral_piramide)
print("#area de la base de la piramide:    ",area_base_piramide)
print("#area total de la piramide     ",area_total_piramide)
print("###################################################")
print("#area total de la piramide=!62",verificador)
