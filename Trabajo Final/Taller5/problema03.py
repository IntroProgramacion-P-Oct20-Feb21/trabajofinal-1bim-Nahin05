valorVenta = 0
impuestoAlemania = 20
impuestoJapon = 30
impuestoItalia = 15
impuestoUsa = 8
costo = float(input("Ingrese el precio del auto\n"))
marca = input("Ingrese la marca del auto\n")
origen = int(input("Seleccione el numero del pais de origen \n1."
                   + "Alemania\n2.Japon\n3.Italia\n4.USA\n"))
if origen == 1:
    impuestoAlemania = 20
    impuesto = (impuestoAlemania * costo / 100)
    valorVenta = (costo + impuesto)
    print(f"El impuesto a pagar es: {impuesto:.2f} y El precio de venta es:"
          f" {valorVenta:.2f}")
if origen == 2:
    impuestoJapon = 30
    impuesto = (impuestoJapon * costo / 100)
    valorVenta = (costo + impuesto)
    print(f"El impuesto a pagar es: {impuesto:.2f} y El precio de venta es:"
          f" {valorVenta:.2f}")
if origen == 3:
    impuestoItalia = 15
    impuesto = (impuestoItalia * costo / 100)
    valorVenta = (costo + impuesto)
    print(f"El impuesto a pagar es: {impuesto:.2f} y El precio de venta es:"
          f" {valorVenta:.2f}")
if origen == 4:
    impuestoUsa = 8
    impuesto = (impuestoUsa * costo / 100)
    valorVenta = (costo + impuesto)
    print(f"El impuesto a pagar es: {impuesto:.2f} y El precio de venta es:"
          f" {valorVenta:.2f}")
