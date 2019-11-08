# INPUT
densidad=int(input("Densidad:"))
altura=int(input("Altura:"))
gravedad=float(input("Gravedad:"))

# PROCESSING
presion=densidad*altura*gravedad
print("Presion:", presion)

# VERIFICADOR
comprobar=(presion<42.3)

# OUTPUT
print("#################################")
print("#    PRESION DE UN CUERPO         ")
print("###################################")
print("#")
print("#  DATOS:             VALOR:      ")
print("# densidad:          ",densidad," ")
print("# altura:            ",altura,"   ")
print("# gravedad:          ",gravedad,"  ")
print("# presion:           ",presion,"  ")
print("###################################")
print("comprobar la presion:", comprobar)
