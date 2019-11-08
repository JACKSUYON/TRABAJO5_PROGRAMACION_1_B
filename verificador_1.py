#verificador 1 :calcular el numero de masa
numero_de_masa, numero_atomico, numero_de_neutrones=0.0, 0.0, 0.0
#asignacion valores de valores
numero_atomico=int(input("mostrar el numero atomico:"))
numero_de_neutrones=int(input("mostrar el numerode neutrones:"))
#calculo
numero_de_masa=(numero_atomico + numero_de_neutrones)
verificador=(numero_de_masa<=60)
#mostrar valores
print("numero atomico:",numero_atomico)
print("numero de neutrones",numero_de_neutrones)
print("numero de masa:",numero_de_masa)
print("numero de masa<=60",verificador)
