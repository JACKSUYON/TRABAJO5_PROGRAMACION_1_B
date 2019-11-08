#verificador 13: calcular la eficiencia
eficiencia, trabajo_util, trabajo_suministrado=0.0, 0.0, 0.0
#asigancion de valores
trabajo_util=int(input("mostrar el trabajo util:"))
trabajo_suministrado=int(input("mostrar el trabao suministrado:"))
#calculo
eficiencia=trabajo_util/trabajo_suministrado
verificador=(eficiencia>47)
#mostrar valores
print("trabajo util:",trabajo_util)
print("trabajo suministrado:",trabajo_suministrado)
print("eficiencia:",eficiencia)
print("eficiencia>47:",verificador)
