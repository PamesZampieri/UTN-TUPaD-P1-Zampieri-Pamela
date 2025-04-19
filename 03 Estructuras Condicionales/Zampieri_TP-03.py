# Programación1
# Práctico 3: Estructuras condicionales
# Nombre y apellido: Pamela Zampieri

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.    

nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")   

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar. 

numero = int(input("Ingrese un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")    

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño")
elif edad >= 12 and edad < 18:    
    print("Adolescente")
elif edad >= 18 and edad < 30:   
    print("Adulto joven")   
else:
    print("Adulto mayor")    

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string. 

contraseña = input("Escriba una contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media 
# y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.   

import random
import statistics  

numeros_aleatorios = [random.randint(1, 100) for i in range (50)]

media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)

print("Números aleatorios:", numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
else:
    print("Sin sesgo significativo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

palabra = input("Escriba a continuación una palabra o frase: ")

if palabra.lower().endswith(('a', 'e', 'i', 'o', 'u')):
    print(f"{palabra}!")
else:
    print(palabra)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")

print("Ingrese la opción deseada: (1-2-3)")
print("1. Nombre en mayúsculas.")
print("2. Nombre en minúsculas.")
print("3. Nombre con la primera letra mayúscula.")

opcionElegida = int(input("Opción: "))

if opcionElegida == 1:
    print(nombre.upper())
elif opcionElegida == 2:
    print(nombre.lower())
elif opcionElegida == 3:
    print(nombre.title())
else:
    print("Opción inválida. Debe elegir 1, 2 o 3.")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitudTerremoto = float(input("Ingrese la magnitud del terremoto: "))

if magnitudTerremoto < 3:
    print("Muy leve (imperceptible).")
elif magnitudTerremoto >= 3 and magnitudTerremoto < 4:
    print("Leve (ligeramente perceptible).")  
elif magnitudTerremoto >= 4 and magnitudTerremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")  
elif magnitudTerremoto >= 5 and magnitudTerremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")      
elif magnitudTerremoto >= 6 and magnitudTerremoto < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")                            

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("¿En qué hemisferio estás? (N/S): ").lower()
mes = input("¿Qué mes es? (ej: marzo): ").lower()
dia = int(input("¿Qué día del mes es?: "))

if mes == "diciembre" and dia >= 21 or mes in ["enero", "febrero"] or (mes == "marzo" and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif mes == "marzo" and dia >= 21 or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif mes == "junio" and dia >= 21 or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif mes == "septiembre" and dia >= 21 or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    estacion_norte = estacion_sur = "No se pudo determinar la estación."

if hemisferio == "n":
    print("Estás en", estacion_norte)
elif hemisferio == "s":
    print("Estás en", estacion_sur)
else:
    print("Hemisferio no válido.")
