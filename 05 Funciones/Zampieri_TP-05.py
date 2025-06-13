# Programación1
# Práctico 5: Funciones en Python
# Nombre y apellido: Pamela Zampieri

# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. 
# Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print ("Hola Mundo!")

# Programa principal

imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y 
# devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), 
# deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa principal

nombre = input("Escriba su nombre: ")
print(saludar_usuario(nombre))

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros 
# e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa principal

nombre = input("Escriba su nombre: ")
apellido = input("Escriba su apellido: ")
edad = input("Escriba su edad: ")
residencia = input("Escriba su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal

radio = float(input("Escriba el radio de un círculo: "))

print(f"Área del círculo: {calcular_area_circulo(radio):.2f}")
print(f"Circunferencia del círculo: {calcular_perimetro_circulo(radio):.2f}")

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro 
# y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal

segundos = int(input("Escriba los segundos: "))

print(f"La cantidad de horas que equivalen los segundos ingresados es de: {segundos_a_horas(segundos):.2f} horas.")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro e 
# imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Programa principal

numero = int(input("Escriba un número para saber su tabla de multiplicar: "))

print(f"\nTabla de multiplicar del {numero}:")
tabla_multiplicar(numero)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva 
# una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b)

# Programa principal

numero1 = int(input("Escriba un número: "))
numero2 = int(input("Escriba otro número: "))

suma, resta, multiplicacion, division = operaciones_basicas(numero1, numero2)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division:.2f}")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, 
# y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar 
# el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso / altura ** 2

# Programa principal

peso = float(input("Ingrese su peso en kilogramos (ejemplo: 70): "))
altura = float(input("Ingrese su altura en metros (ejemplo: 1.75): "))

print(f"Su índice de masa corporal es: {calcular_imc(peso, altura):.2f}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y 
# devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return (9 / 5) * celsius + 32

# Programa principal

temperaturaEnCelsius = float(input("Ingrese una temperatura en grados Celsius (ºC): "))

print(f"La temperatura en Fahrenheit es: {celsius_a_fahrenheit(temperaturaEnCelsius):.2f} ºF")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal

numero1 = float(input("Escriba el primer número: "))
numero2 = float(input("Escriba el segundo número: "))
numero3 = float(input("Escriba el tercer número: "))

print(f"El promedio es: {calcular_promedio(numero1, numero2, numero3):.2f}")