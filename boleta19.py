# INPUT
Masa=int(input("Masa:"))
Aceleracion=int(input("Aceleracion:"))

# PROCESSING
Fuerza=Masa*Aceleracion
print("Fuerza:", Fuerza)

# VERIFICADOR
comprobar=(Fuerza<=80)

# OUTPUT
print("################################################")
print("  LA FUEZA QUE APLICA UNA PERSONA A UNA PIEDRA  ")
print("################################################")
print("#")
print("# DATOS:                 VALOR:                ")
print("# Masa:                 ", Masa , "            ")
print("# Aceleracion:         ", Aceleracion , "      ")
print("# Fuerza:              ",Fuerza ,"             ")
print("###############################################")
print("comprobar la fuerza:" , comprobar              )
