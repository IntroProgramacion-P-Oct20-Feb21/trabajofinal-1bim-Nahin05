nombreCliente = input("Ingrese el nombre del cliente\n")
numMensualidades = int(input("Cuantas mensualidades va a cancelar\n"))
contador = 1
valor = 0
cadenaFinal = ""
while contador <= numMensualidades:
    print("\nSeleccione la empresa a la que va a cancelar\n"
          "Netflix\n"
          "Disney Plus \n"
          "Apple TV ")
    empresa = input("Amazon Prime\n")
    if empresa == "Netflix":
        valor = 10
        iva = (valor * 10) / 100
        totalCancelar = valor + iva
        cadenaFinal = "Usuario: %s\n" \
                      "Empresa: %s " \
                      "\nPrecio " \
                      "base: $%.2f\n" \
                      "Impuesto: $%.2f\n" \
                      "Total a cancelar: $%.2f\n" \
                      "" % \
                      (nombreCliente, empresa, valor, iva, totalCancelar)

    elif empresa == "Disney Plus":
        iva = (valor * 12) / 100
        totalCancelar = valor + iva
        cadenaFinal = "Usuario: %s\n" \
                      "Empresa: %s " \
                      "\nPrecio " \
                      "base: $%.2f\n" \
                      "Impuesto: $%.2f\n" \
                      "Total a cancelar: $%.2f\n" \
                      "" % \
                      (nombreCliente, empresa, valor, iva, totalCancelar)

    elif empresa == "Apple TV":
        valor = 5
        iva = (valor * 14) / 100
        totalCancelar = valor + iva
        cadenaFinal = "Usuario: %s\n" \
                      "Empresa: %s " \
                      "\nPrecio " \
                      "base: $%.2f\n" \
                      "Impuesto: $%.2f\n" \
                      "Total a cancelar: $%.2f\n" \
                      "" % \
                      (nombreCliente, empresa, valor, iva, totalCancelar)

    elif empresa == "Amazon Prime":
        valor = 4.50
        iva = (valor * 16) / 100
        totalCancelar = valor + iva
        cadenaFinal = "Usuario: %s\n" \
                      "Empresa: %s " \
                      "\nPrecio " \
                      "base: $%.2f\n" \
                      "Impuesto: $%.2f\n" \
                      "Total a cancelar: $%.2f\n" \
                      "" % \
                      (nombreCliente, empresa, valor, iva, totalCancelar)

    contador = contador + 1
    print("%s" % cadenaFinal)
