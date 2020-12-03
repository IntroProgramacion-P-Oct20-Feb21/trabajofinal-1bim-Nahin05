valorDescuento = 15
precioUnitario = float(input("Ingrese el costo por unidad\n"))
cantidad = int(input("Ingrese el numero de unidades\n"))
costo = precioUnitario * cantidad
if cantidad > 50:
    descuento = (costo * valorDescuento) / 100
    costo = costo - descuento
print("El costo con el 15 de descuento: %.2f" % costo)