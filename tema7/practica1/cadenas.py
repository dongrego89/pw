cadena1="Esta es la primera cadena"
cadena2="Esta es la segunda cadena"

cadena3=cadena1+" "+cadena2
cadena4=cadena3[:10]

cadena5="ejemplo de cadena".upper()
cadena6="ejemplo de cadena".lower()
cadena7="ejemplo de cadena".capitalize()
cadena8="\n\tejemplo de cadena".strip()

import string
string.letters
string.digits
string.punctuation

def cuentaPalabras(cadena):
    return len(cadena.split())
