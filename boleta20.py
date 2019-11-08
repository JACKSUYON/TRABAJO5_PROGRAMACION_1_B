# INPUT
base_mayor=int(input("base mayor:"))
base_menor=int(input("base menor:"))
altura=int(input("altura:"))

# PROCESSING
area_del_trapecio=((base_mayor+base_menor)*altura)/2
print("area del trapecio:", area_del_trapecio)

# VERIFICADOR
comprobar_area=(area_del_trapecio>=546)

# OUTPUT
print("###############################")
print("    AREA DEL TRAPECIO           ")
print("####################################")
print("#")
print("#  DATOS:                VALOR:      ")
print("#  Base mayor:         ",base_mayor," ")
print("#  Base menor:         ",base_menor," ")
print("#  Altura:             ",altura,"     ")
print("#  Area trapecio:      ",area_del_trapecio," ")
print("#######################################")
print("comprobar el area del trapecio:",comprobar_area)
