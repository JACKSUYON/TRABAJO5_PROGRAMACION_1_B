#boleta 3 : calcular la densidad

#input
cuerpo=input("ingrese el cuerpo: ")
masa=int(input("ingrese la masa:"))
volumen=float(input("ingrese el volumen:"))

#processing
densidad=masa/volumen

#verificador
verificador=(densidad==45)

#output
print("#####################################")
print("#     BOLETA FORMULA DENSIDAD        #")
print("######################################")
print("#   datos")
print("#tipo de cuerpo:  ",cuerpo            )
print("#masa: ",masa                         )
print("#volumen:  ",volumen                  )
print("#densidad:   ",densidad               )
print("#######################################")
print("#densidad==45:   ",verificador        )
