# INPUT
cliente=input("nombre del cliente:")
pedido01=int(input("Nro de camisas:"))
pedido02=int(input("Nro de pantalones:"))
pedido03=int(input("Nro de corbatas:"))
pu1=float(input("precio unitario camisas:"))
pu2=float(input("precio unitario pantalones:"))
pu3=float(input("precio unitario corbatas:"))
IGV=8.8

# PROCESSING
total=(pedido01*pu1+pedido02*pu2+pedido03*pu3)+IGV

# VERIFICADOR
comprobar=(total>=894)

# OUTPUT
print("######################################")
print("    BOLETA DE VENTA : TIENDA JOSE             ")
print("###########################################")
print("#")
print("# cliente:              ",cliente,"    ")
print("# camisas:              ",pedido01,"   ")
print("  pu camisas:           ",pu1,"        ")
print("# pantalones:           ",pedido02,"   ")
print("  pu pantalones:        ",pu2,"        ")
print("# corbatas:             ",pedido03,"   ")
print("  pu corbatas:          ",pu3,"        ")
print("# IGV:                  ",IGV,"        ")
print("# total:                ",total,"      ")
print("###########################################")
print(" comprovar:", comprobar)
