# INPUT
nombre=input("nombre:")
cargo=input("cargo:")
sueldo=int(input("sueldo mensual:"))
descuento=float(input("descuento del AFP:"))

# PROCESSING
total_salario_mensual=sueldo-(descuento*sueldo)

# VERIFICADOR
comprobar_el_sueldo=(total_salario_mensual<45.85)

# OUTPUT
print("##########################################")
print("       BOLETA DE PAGO                 ")
print("#########################################")
print("#")
print("# Nombre:                  ",nombre,"    ")
print("# Cargo:                   ",cargo,"     ")
print("# sueldo mensual:          ",sueldo,"    ")
print("# descuento del AFP:       ",descuento," ")
print("# total de recibo mensual: ",total_salario_mensual," ")
print("#############################################")
print("comprobando:"   ,comprobar_el_sueldo)
