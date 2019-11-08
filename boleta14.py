# INPUT
masa=int(input("Masa:"))
volumen=int(input("volumen:"))

# PROCESSING
Densidad=masa/volumen
print("densidad:", Densidad)

# VERIFICADOR
comprobador=(Densidad>=80)

# OUTPUT
print("#####################################")
print("#      DENSIDAD DE UN CUERPO      ")
print("######################################")
print("#")
print("# DATOS:             VALOR:   ")
print("# masa:             ",masa,"     ")
print("# volumen:          ",volumen,"   ")
print("# densidad:         ",Densidad,"   ")
print("######################################")
print(" comprobar la densida del cuerpo:", comprobador)
