#verificador 14: calcular la rapidez media
rapidez_media, distancia_recorrida, tiempo_transcurrido=0.0, 0.0, 0.0
#asigancion de valores
distancia_recorrida=int(input("mostrar distancia recorrida:"))
tiempo_transcurrido=int(input("mostrar el tiempo transcurrido:"))
#calculo
rapidez_media=distancia_recorrida/tiempo_transcurrido
verificador=(rapidez_media==31)
#mostrar valores
print("distancia recorrida:",distancia_recorrida)
print("tiempo transcurrido:",tiempo_transcurrido)
print("rapidez media:",rapidez_media)
print("rapidez media==31",verificador)
