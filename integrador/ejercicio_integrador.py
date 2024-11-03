mayor_precio_flag = True
mayor_cantidad_de_unidades_flag = True
cantidad_unidades_barbijo_mas_caro = 0
acumulador_total_jabones = 0

for numero in range(5):
    tipo = input("Ingrese un tipo de producto de prevención de contagio: ")
    while tipo != "barbijo" and tipo != "jabón" and tipo != "alcohol":
        tipo = input("Error. Ingrese un tipo de producto de prevencion de contagio valido: ")
    precio = int(input("Ingrese un precio: "))
    while precio < 100 or precio > 300:
        precio = int(input("Error. Ingrese un precio válido: "))
    cantidad_de_unidades = int(input("Ingrese cantidad de unidades"))
    while cantidad_de_unidades <= 0 or cantidad_de_unidades > 1000:
        cantidad_de_unidades = int(input("Error. Ingrese una cantidad de unidades válida"))
    fabricante = input("Ingrese el fabricante: ")
    if tipo == "barbijo":
        if mayor_precio_flag == True or precio > mayor_precio:
            mayor_precio = precio
            fabricante_barbijo_mas_caro = fabricante
            cantidad_unidades_barbijo_mas_caro = cantidad_de_unidades
            mayor_precio_flag = False
    if tipo == "jabón":
        acumulador_total_jabones += cantidad_de_unidades
    if mayor_cantidad_de_unidades_flag == True or cantidad_de_unidades > mayor_cantidad_de_unidades:
        mayor_cantidad_de_unidades = cantidad_de_unidades
        fabricante_mayor_cantidad_de_unidades = fabricante
        mayor_cantidad_de_unidades_flag = False 
    
print("El más caro de los barbijos tiene una cantidad de ",cantidad_unidades_barbijo_mas_caro," y es fabricado por ", fabricante_barbijo_mas_caro)
print("El fabricante con más unidades es ", fabricante_mayor_cantidad_de_unidades," y la mayor cantidad de unidades en un ítem es ", mayor_cantidad_de_unidades)
print("La cantidad total de jabones es ", acumulador_total_jabones)