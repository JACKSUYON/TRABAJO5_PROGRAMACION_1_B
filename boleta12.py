# INPUT
cliente=input("cliente:")
paga=int(input("monto:"))
interes=float(input("interes:"))
dia=input("Dia:")

# PROCESSING
total_a_pagar=paga+interes*paga

# VERIFICADOR
comprobando_total=(total_a_pagar<465)

# OUTPUT
print("#####################################")
print("  BOLETA ELECTRONICA            ")
print("#")
print(" cliente:      ",cliente,"      ")
print("#")
print("# Dia:           ",dia,"        ")
print("# pagar:         ",paga,"       ")
print("# interes:       ",interes,"    ")
print("# total a pagar:  ",total_a_pagar," ")
print("#################################")
print(" comprobando :" , comprobando_total)
