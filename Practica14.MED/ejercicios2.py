import re

def buscar_fecha(cadena):
    patron = r"\b\d{2}/\d{2}/\d{4}\b"
    if re.search(patron, cadena):
        return True
    else:
        return False
cadena1 = "Hoy es 29/11/2023"
cadena2 = "La fecha límite es el 30/12/2022"
cadena3 = "No hay fechas en esta cadena"

print(buscar_fecha(cadena1))
print(buscar_fecha(cadena2))
print(buscar_fecha(cadena3))
