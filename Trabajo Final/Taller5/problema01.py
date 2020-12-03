valorPorcentaje = 10
kilovatioHora = float(input("Ingrese el valor de costo del kilovatio por hora\n"))
valorConsumido = int(input("Ingrese los kilovatios consumidos en el mes\n"))
edadCliente = int(input("Ingrese la edad del cliente\n"))
valorTotal = kilovatioHora * valorConsumido
if edadCliente > 65:
    descuento = (valorTotal * valorPorcentaje) / 100
    valorTotal = valorTotal - descuento
print("El costo total es: %.2f" % valorTotal)
