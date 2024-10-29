from biblioteca import *

# Desarrollar en Python:

# Crear una biblioteca que contenga las siguientes funciones:

# Desarrollar una función que genere de manera aleatoria una lista alfanumérica de mil (1000) elementos cuyos caracteres podrán ser los siguientes 0-9 A-Z 
# (del ‘0’ al ‘9’ y de la ‘A’ a la ‘Z’).

# Desarrollar una función que genere de manera aleatoria una matriz de 10 filas por 10 columnas (10 listas de 10 elementos cada una), de números enteros.

# Desarrollar una función que ordene una lista de números enteros, recibiendo como parámetro el criterio de ordenamiento ASC o DESC.

# Desarrollar una función que valide el ingreso de un número entero, para ser utilizada en el ítem 6.
# Luego, se deberá programar un menú de opciones operado por consola, que realice lo siguiente:

# 1 – Generar la lista alfanumérica aleatoria utilizando la función desarrollada.

# 2 – Ordenar la lista alfanumérica generada anteriormente, utilizando la función desarrollada.

# 3 – Buscar e informar cuantas veces se repite cada uno de los caracteres alfabéticos A-Z (de la ‘A’ a la ‘Z’).

# El informe deberá realizarse con un registro debajo del otro y el mismo tendrá el siguiente encabezado:

# CARACTER | CANTIDAD

# 4 – Del ítem anterior, obtener:

    # El caracter que más veces se repite e informar la cantidad.
    # El caracter que menos veces se repite e informar la cantidad.

# 5 – Generar la matriz aleatoria de números enteros, utilizando la función desarrollada.

# 6 – Se debe ingresar una secuencia numérica (de dos dígitos como mínimo), por consola, validando que la misma corresponda a un número entero.

# Luego buscar (de manera horizontal), en la matriz si existe la secuencia numérica ingresada en el ítem anterior.

# Por último informar:

# En caso negativo informar por pantalla: “La secuencia numérica <secuencia numérica> no existe en la matriz.
# En caso positivo, informar por pantalla: “La secuencia numérica <secuencia numérica> existe en la matriz.

# 7 – Salir.

# Menu
flag = False
flag_2 = False

while True:
    match menu_4_case(
        "1- [Generar lista alfanumerica aleatoria]",
        "2- [Ordenar la lista alfanumérica generada]",
        "3- {Buscar e informar cuantas veces se repite cada uno de los caracteres alfabéticos A-Z]",
        "4- [Caracter mas repetido y menos repetido]",
        "5- [Generar matriz aleatoria]",
        "6- [Buscar secuencia numerica y informar]",
        "7- [Salir]"):
        case "1":
            lista_alfanumerica = generar_lista_random_alfanumerica(1000)
            flag = True
        case "2":
            if not flag:
                print("No puede ordenar los datos si no genera una lista aleatoria!")
            else:
                criterio = input("Ingrese criterio de ordenamiento: ")
                while (criterio != "asc" and criterio != "dsc") and (criterio != "ASC" and criterio != "DSC"):
                    criterio = input("ERROR! Solo elegir 'asc' o 'dsc'. Ingrese criterio de ordenamiento: ")
                ordenar_lista(lista_alfanumerica, criterio)
        case "3":
            if not flag:
                print("ERROR! Primero debe generar la lista alfanumerica!")
            else:
                conteo = contar_caracteres(lista_alfanumerica)
                mostrar_resultado_punto_3(conteo)
        case "4":
            if not flag:
                print("ERROR! Primero debe generar la lista alfanumerica!")
            else:
                lista_minimo = buscar_valor_minimo_y_maximo(lista_alfanumerica, "max")
                lista_maximo = buscar_valor_minimo_y_maximo(lista_alfanumerica, "min")
                mostrar_resultado_punto_4(lista_minimo, lista_maximo)
        case "5":
            matriz_aleatoria = crear_matriz_aleatoria(10, 10, 1, 10)
            flag_2 = True
        case "6":
            if not flag_2:
                print("ERROR! Primero debe generar la matriz!")
            else:
                print(matriz_aleatoria)
                digit = input("Ingrese una secuencia numerica: ")
                while not validar_numero_entero(digit):
                    digit = input("Ingrese una secuencia numerica: ")
                busqueda_digito = buscar_secuencia(matriz_aleatoria, digit)
        case "7":
            opcion = input("Confirma que quiere salir?: ")
            resultado = confirmar_salir(opcion)
            if resultado:
                break
    pausar()
