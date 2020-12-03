numerador = 1
denominador = 1
contador = 1
cadenaFinal = ""
while contador <= 8:
    if (contador % 2) == 0:
        cadenaFinal = "%s -%d/%d " % (cadenaFinal, numerador, denominador)
    else:
        cadenaFinal = "%s +%d/%d " % (cadenaFinal, numerador, denominador)
    contador = contador + 1
    denominador = denominador + 2
print(cadenaFinal)
