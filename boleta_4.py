#boleta 4: calcular el area lateral de un cono
#input
pi=3.1416
radio=float(input("mostrar el radio:"))
generatriz=int(input("mostrar generatriz:"))

#processing
area_lateral_cono=(pi*radio*generatriz)
verificador=(area_lateral_cono<=65)

#output
print("###########################################")
print("#       BOLETA DEL AREA LATERAL DEL CONO   #" )
print("############################################" )
print("#    datos"                                     )
print("#pi:   ",pi                                 )
print("#radio:  ",radio                            )
print("#generatriz:  ",generatriz                  )
print("#area lateral del cono:  ",area_lateral_cono)
print("###########################################")
print("#area lateral del cono<=65:",verificador)
