# 10) Desarrollar una función que verifique el DNI de una persona, la misma recibirá una cadena de caracteres
# (se asume que solamente contiene caracteres numéricos). Si la cantidad de caracteres es menor a 6 o
# mayor a 8, retornara False. Si la cantidad de caracteres está comprendida entre 6 y 8 devolverá True.

from biblioteca import *

mensaje = "Ingrese el DNI: "
numero = input(mensaje)
while validar_numero_entero(numero) != True:
    numero = input(mensaje)
print(validar_dni(numero))
