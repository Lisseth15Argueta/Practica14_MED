import re

def encontrar_palabras_minusculas(texto):
    patron = r'\b[a-z]+\b'
    palabras = re.findall(patron, texto)
    return palabras

texto = "Este es Un textos de Palabras que Contiene solo Minusculas"
palabras = encontrar_palabras_minusculas(texto)
print(palabras)