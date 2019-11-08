#boleta 7: clacular el area lateral del cilindro
#input
pi=3.1416
radio1=float(input("ingrese el radio:"))
generatriz1=int(input("ingrese la generatriz:"))

#processing
area_lateral_cilindro=(2*pi*radio1*generatriz1)

#verificador
verificador=(area_lateral_cilindro>=29)

#output
print("###############################################")
print("#         BOLETA DEL AREA DEL CILINDRO        #")
print("###############################################")
print("#   datos")
print("#pi:  ",pi                                       )
print("#radio1:    ",radio1)
print("#generatriz1:    ",generatriz1)
print("#area latera del cilindro:    ",area_lateral_cilindro)
print("#################################################")
print("#area lateral del cilindro>=29",verificador)
