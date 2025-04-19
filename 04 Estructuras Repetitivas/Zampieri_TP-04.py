# Programación1
# Práctico 4: Estructuras repetitivas
# Nombre y apellido: Pamela Zampieri

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.   

numero = int(input("Ingrese un número entero: "))
numero = abs(numero)

contador = 0

if numero == 0:
    contador = 1
else:
    while numero > 0:
        numero = numero // 10  
        contador += 1

print("El número tiene", contador, "dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

bandera1 = int(input("Ingrese un número entero: "))
bandera2 = int(input("Ingrese otro número entero: "))
sumatoria = 0

inicio = min(bandera1, bandera2)
fin = max(bandera1, bandera2)

for i in range(inicio + 1, fin): 
    sumatoria += i

print("El total de la suma de todos los números enteros comprendidos entre", bandera1, "y", bandera2, "=", sumatoria)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

CORTE = 0

numero = int(input(f"Ingrese un número o {CORTE} para terminar: "))
sumatoria = 0

while numero != 0:
    sumatoria += numero
    numero = int(input(f"Ingrese otro número o {CORTE} para terminar: "))

print("El total de la suma de los números ingresados es: ", sumatoria)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numerosDeLaSuerte = random.randint(0, 9)

print("¡Bienvenido al juego! Adivina el número entre 0 y 9.")
numero = int(input("Ingrese un número del 0 al 9: "))

if(numero < 0 or numero > 9):
    print("Usted ha ingresado un número inválido.")
else:
    contador = 1

    while numero != numerosDeLaSuerte:
        numero = int(input("Ingrese otro número: "))
        contador += 1

    print(f"¡Adivinó el número de la suerte en {contador} intentos!")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

bandera = int(input("Ingrese un número entero: "))
sumatoria = 0

if bandera <= 0:
    print("Usted ingresó un número inválido.")
else:
    for i in range(bandera + 1): 
        sumatoria += i
    
    print(f"El total de la suma de todos los números enteros comprendidos entre 0 y {bandera}:", sumatoria)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

CANTIDAD_NUMEROS = 100 # Las pruebas las hice con 5 números 
numerosPares = 0
numerosImpares = 0
numerosPositivos = 0
numerosNegativos = 0

for i in range(CANTIDAD_NUMEROS):
    numero = int(input("Ingrese un número entero: "))

    if numero % 2 == 0:
        numerosPares += 1
    else:
        numerosImpares += 1
    
    if numero > 0:
        numerosPositivos += 1
    elif numero < 0:
        numerosNegativos += 1 

print("Cantidad de números pares: ", numerosPares)
print("Cantidad de números impares: ", numerosImpares)
print("Cantidad de números positivos: ", numerosPositivos)
print("Cantidad de números negativos: ", numerosNegativos)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

import statistics  

CANTIDAD_NUMEROS = 100 # Las pruebas las hice con 5 números 
numerosIngresados = [] 

for i in range(CANTIDAD_NUMEROS):
    numero = int(input("Ingrese un número entero: ")) 
    numerosIngresados.append(numero)

if len(numerosIngresados) > 0:
    media = statistics.mean(numerosIngresados)
    print("La media de los números ingresados es:", media)
else:
    print("No se ingresaron números para calcular la media.")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese un número: "))
numeroInvertido = 0

while numero > 0:
    digito = numero % 10  
    numeroInvertido = numeroInvertido * 10 + digito 
    numero = numero // 10 

print("El número invertido es:", numeroInvertido)
