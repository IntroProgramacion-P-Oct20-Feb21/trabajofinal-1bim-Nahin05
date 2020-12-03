plazo = 12
valorPrestamo = float(input("Ingrese valor del Prestamo\n"))
valorInteres = float(input("Ingrese valor del Interes\n"))
valorTotal = (valorPrestamo / plazo) + valorInteres
print("La mensualidad es: %2.f" % valorTotal)
