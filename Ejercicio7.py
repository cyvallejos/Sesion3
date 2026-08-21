precio = float(input("Ingrese el precio del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

descuento = precio * (porcentaje_descuento / 100)
precio_final = precio - descuento

print(f"El descuento aplicado es: {descuento}")
print(f"El precio final es: {precio_final}")
