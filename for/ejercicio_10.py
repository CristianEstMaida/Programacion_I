#  10. Ingresar un número.
# Determinar si el número es primo o no.

numero = int(input("Ingrese un número: "))
contador = 0
es_primo = True

if numero < 2:
    es_primo = False

for i in range(1, numero + 1):
    if numero % i == 0:
        contador += 1
    if contador > 2:
        es_primo = False
        break
    
if es_primo:
    print("Es primo")
else:
    print("No es primo")