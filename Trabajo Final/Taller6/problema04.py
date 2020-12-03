contador = 1
cadenaFinal = ""
while contador <= 10:
    nombreJugador = input("Ingrese el nombre del jugador: \n")
    puntosAnotados = int(input("Ingrese la cantidad de puntos "
                               "que anoto en la temporada\n"))
    faltasCometidas = int(input("Ingrese la cantidad de faltas cometidas:\n"))
    cadenaFinal = "%s%s\t%d\t%d\n" % (cadenaFinal, nombreJugador, puntosAnotados, faltasCometidas)
    contador = contador + 1
print("%s" % cadenaFinal)
