#boleta 6: calcular el volumen de la piramide
#input
area_base_de_la_piramide=int(input("ingrese el area de la base:"))
altura=float(input("ingrese la altura:"))

#processing
volumen_piramide=(area_base_de_la_piramide*altura)/3

#verificador
verificador=(volumen_piramide>36)

#output
print("##################################################")
print("#       BOLETA DEL VOLUMEN DE UNA PIRAMIDE   #")
print("##################################################")
print("#datos")
print("#area de la base de la piramide:",area_base_de_la_piramide)
print("#altura:",altura)
print("#volumen de la piramide:",volumen_piramide)
print("###################################################")
print("#volumen de la piramide>36",verificador)
