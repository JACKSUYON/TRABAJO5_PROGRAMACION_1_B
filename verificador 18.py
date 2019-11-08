#verificador 18: calcular la calga de un cuerpo
carga_del_cuerpo, carga_del_electron, numero_entero=0.0, 0.0, 0.0
#asigancion de valores
carga_del_electron=int(input("mostrar carga del electron:"))
numero_entero=int(input("mostrar numero entero:"))
#calculo
carga_del_cuerpo=numero_entero*carga_del_electron
verificador=(carga_del_cuerpo>13)
#mostrar valores
print("carga del electron:",carga_del_electron)
print("numero entero:",numero_entero)
print("carga del cuerpo:",carga_del_cuerpo)
print("carga del cuerpo>13:",verificador)
