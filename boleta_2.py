#boleta 2 :calcular el numero de electrones
#input
numero_de_protones=int(input("ingre el numero de protones:"))
carga=int(input("ingrese la carga:"))

#processing
numero_de_electrones=(numero_de_protones + carga)

#verificador
verificador=(numero_de_electrones>47)

#output
print("###########################################")
print("#      BOLETA DE NUMERO DE ELECTRONES     #")
print("###########################################")
print("#   datos  ")
print("#numero de protones:",numero_de_protones)
print("#carga:",carga)
print("#numero de elctrones es:",numero_de_electrones)
print("###########################################")
print("#el numero de elctrones>47:",verificador)
