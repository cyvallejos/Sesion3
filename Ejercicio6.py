from datetime import datetime

anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
anio_actual = datetime.now().year

edad = anio_actual - anio_nacimiento

print(f"Su edad aproximada es: {edad} años")
