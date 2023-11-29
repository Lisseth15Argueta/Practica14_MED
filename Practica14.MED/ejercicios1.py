import re

def verificar_codigo_empleado(cadena):
    patron = r"^EMP"
    if re.match(patron, cadena):
        return True
    else:
        return False
cadena1 = "EMP123"
cadena2 = "EMP4567"
cadena3 = "EM123"
cadena4 = "EMPABC"

print(verificar_codigo_empleado(cadena1))
print(verificar_codigo_empleado(cadena2))
print(verificar_codigo_empleado(cadena3))
print(verificar_codigo_empleado(cadena4))
