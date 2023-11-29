import re

def ocurrencia(texto, palabra):
    patron = r'\b' + re.escape(palabra) + r'\b'
    coincidencias = re.finditer(patron, texto)
    ubicaciones = [coincidencia.span() for coincidencia in coincidencias]
    return ubicaciones

texto = "Este es un ejemplo de texto con varias ocurrencias de la palabra ejemplo"
palabra = "ejemplo"
ocurrencias = ocurrencia(texto, palabra)
print(ocurrencias)
