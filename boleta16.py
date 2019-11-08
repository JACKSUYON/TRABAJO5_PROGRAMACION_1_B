# INPUT
Radio=int(input("Radio:"))
Pi=float(input("Pi:"))

# PROCESSING
area=((Radio**2)*Pi)
print("area:",area)

# VERIFICADOR
comprobador=(area>=145)

# OUTPUT
print("####################################")
print("#      AREA DEL CIRCULO          ")
print("######################################")
print("#")
print("#  DATOS:                 VALOR:   ")
print("# radio:                ",Radio,"   ")
print("# Pi:                   ",Pi,"      ")
print("# Area:                 ",area,"    ")
print("#####################################")
print("comprobar el area del circulo:", comprobador)
