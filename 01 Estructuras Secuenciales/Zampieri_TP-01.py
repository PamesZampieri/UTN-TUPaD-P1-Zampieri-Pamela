# Programación1
# Práctico 1: Estructuras secuenciales
# Nombre y apellido: Pamela Zampieri

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
import math

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input ("Por favor escriba su nombre: ")

print(f"Hola {nombre} espero que tengas un hermoso día!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre = input ("Escriba su nombre: ")
apellido = input ("Escriba su apellido: ")
edad = input ("Escriba su edad: ")
lugarDeResidencia = input ("Escriba su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarDeResidencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float(input("Escriba el radio de un círculo: "))

area = math.pi * radio ** 2 
perimetro = 2 * math.pi * radio

print(f"Área del círculo: {area:.2f}")
print(f"Circunferencia del círculo: {perimetro:.2f}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = int(input("Escriba los segundos: "))
horas = segundos / 3600

print(f"La cantidad de horas que equivalen los segundos ingresados es de: {horas:.2f} horas.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Escriba un número para saber su tabla de multiplicar: "))

print(f"\nTabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = int(input("Escriba un número distinto de cero (0): "))
numero2 = int(input("Escriba otro número distinto de cero (0): "))

suma = numero1 + numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2
resta = numero1 - numero2

print(f"\nEl resultado de sumar {numero1} + {numero2} = {suma}")
print(f"\nEl resultado de dividir {numero1} / {numero2} = {division}")
print(f"\nEl resultado de multiplicar {numero1} * {numero2} = {multiplicacion}")
print(f"\nEl resultado de restar {numero1} - {numero2} = {resta}")


# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. 

altura = float(input("Ingrese su altura en metros (ejemplo: 1.75): "))
peso = float(input("Ingrese su peso en kilogramos (ejemplo: 70): "))

indiceDeMasaCorporal = peso / altura ** 2

print(f"Su índice de masa corporal es: {indiceDeMasaCorporal:.2f}")


# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. 

temperaturaEnCelsius = float(input("Ingrese una temperatura en grados Celsius (ºC): "))

fahrenheit = (9 / 5) * temperaturaEnCelsius + 32

print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f} ºF")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

numero1 = float(input("Escriba un número: "))
numero2 = float(input("Escriba otro número: "))
numero3 = float(input("Escriba otro número: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio de los tres números ingresados es: {promedio:.2f}")