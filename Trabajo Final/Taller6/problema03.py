contador = "si"
cadenaFinal = ""
while contador == "si":
    nombre = input("Ingrese el nombre del empleado\n>")
    nombre = input("Ingrese el nombre del empleado\n>")
    numeroDias = int(input("Ingrese el número de días trabajados\n>"))
    costoDia = float(input("Ingrese el costo del día trabajado\n>"))
    pagar = numeroDias * costoDia
    cadenaFinal = "%s%s\t%d\t$%.2f\t\t$%.2f\n" % \
                  (cadenaFinal, nombre, numeroDias, costoDia, pagar)
    contador = input("Ingrese si, en caso de colocar mas empleados\n"
                      "o\n"
                      "Ingrese no, si ya desea ver la tabla\n")
print("%s" % cadenaFinal)
