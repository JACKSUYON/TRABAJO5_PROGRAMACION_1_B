#verificador 15: calcular la direccion
direccion, velocidad, rapidez=0.0, 0.0, 0.0
#asigancion de valores
velocidad=int(input("mostrar la velocidad:"))
rapidez=int(input("mostrar la rapidez:"))
#calculo
direccion=velocidad-rapidez
verificador=(direccion<=29)
#mostrar valores
print("velocidad:",velocidad)
print("rapidez:",rapidez)
print("direcion:",direccion)
print("direccion<=29",verificador)
