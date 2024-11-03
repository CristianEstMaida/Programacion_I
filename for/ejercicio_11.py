#  11. Ingresar un número.
# Mostrar cada número primo que hay entre el 1 y el
#  número ingresado.
#  Informar cuántos números primos se encontraron


numero = int(input("Ingrese un número: "))
contador_primos = 0
for j in range(1, numero + 1):
    contador = 0
    
    es_primo = True
    
    if j < 2:
        es_primo = False
    
    for i in range(1, numero + 1):
        if j % i == 0:
            contador += 1
        if contador > 2:
            es_primo = False
            break
        
    if es_primo:
        contador_primos += 1
        print(f"{j} es primo")
print(f"Se encontraron {contador_primos} números primos")