# INPUT
velocidad_inicial=int(input("Velocidad inicial:"))
velocidad_final=int(input("Velocidad final:"))
tiempo=int(input("Tiempo:"))

# PROCESSING
altura=((velocidad_inicial+velocidad_final)/2)*tiempo
print("Altura:", altura)

# VERIFICADOR
comprobador=(altura>=80)

# OUTPUT
print("##################################")
print("# ALTURA DE UN CUERPO EN CAIDA LIBRE  ")
print("####################################")
print("#")
print("# DATOS:                   VALOR:           ")
print("# velocidad inicial:      ",velocidad_inicial,"  ")
print("# velocidad final:        ",velocidad_final,"   " )
print("# tiempo:                 ",tiempo,"             ")
print("# altura:                 ",altura,"             ")
print("##################################################")
print("comprobar la altura:", comprobador)


