from biblioteca import *

mensaje = "Ingrese un número: "
numero = input(mensaje)
while validar_numero_entero(numero) != True:
    numero = input(mensaje)
if largo_cadena(numero) <= 3:
    print(transformar_numero_a_letras(numero))