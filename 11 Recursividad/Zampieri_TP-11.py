# Programación1
# Práctico 11: Recursividad
# Nombre y apellido: Pamela Zampieri

# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial_recursivo(numero):
    return 1 if numero == 0 else numero * factorial_recursivo(numero - 1)

# Programa principal 

numero = int(input(f"Ingrese un número: "))

print(f"Los factoriales desde 1 hasta {numero} son:")
for i in range(1, numero + 1):
    print(f"{i}! = {factorial_recursivo(i)}")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci_recursivo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)
    
# Programa principal

posicion = int(input(f"Ingrese un número: "))

print(f"La serie de Fibonacci hasta la posición {posicion} es:")
for i in range(posicion + 1):
    print(f"F({i}) = {fibonacci_recursivo(i)}")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1)
# Prueba esta función en un algoritmo general.

def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)
    
# Programa principal

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

print(f"{base}^{exponente} = {potencia_recursiva(base, exponente)}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario 
# como una cadena de texto.

def binario_recursivo(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return binario_recursivo(numero // 2) + str(numero % 2)

# Programa principal

numero = int(input("Ingrese un número entero decimal: "))

print(f"El número {numero} en binario es: {binario_recursivo(numero)}")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[len(palabra) - 1]:
        return False
    
    return es_palindromo(palabra[1: len(palabra) - 1]) 

# Programa principal

palabra = input("Escriba una cadena de texto sin espacios ni tildes: ")

print(f"La cadena {palabra} es palíndromo: {es_palindromo(palabra)}")

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(numero):
    if numero <= 0:
        return 0
    else:
        return numero % 10 + suma_digitos(numero // 10)
    
# Programa principal

numero = int(input("Escriba un número entero positivo: "))

print(f"El total de la suma de los dígitos del número {numero} es: {suma_digitos(numero)}")

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), 
# y así sucesivamente hasta llegar al último nivel con un solo bloque. Escribí una función recursiva contar_bloques(n) que reciba el 
# número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.
#  Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# Programa principal

bloques = int(input("Escriba el número de bloques: "))

print(f"Necesitás un total de {contar_bloques(bloques)} bloques para construir toda la pirámide.")

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito 
# (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4 
# contar_digito(123456, 7) → 0 

def contar_digito(numero, digito):
    if numero <= 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

# Programa principal

numero = int(input("Escriba un número entero positivo: "))
digito = int(input("Escriba un dígito entre 0 y 9: "))

print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en el número: {numero}.")
