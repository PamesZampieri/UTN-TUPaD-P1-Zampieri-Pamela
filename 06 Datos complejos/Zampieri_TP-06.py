# Programación1
# Práctico 6: Estructuras de datos complejas 
# Nombre y apellido: Pamela Zampieri

# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}

for i in range(5):
    nombre = input("Ingrese el nombre de la persona que desea agendar: ")
    telefono = input("Ingrese su número de teléfono: ")

    contactos[nombre] = telefono

nombre_buscado = input("Ingrese el nombre que desea buscar: ")

if nombre_buscado in contactos:
    print(f"Su número telefónico es: {contactos[nombre_buscado]}")
else:
    print("Esta persona no se encuentra agendada.")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)

print(palabras_unicas)

cantidad_palabras = {}

for palabra in palabras:
    cantidad_palabras[palabra] = cantidad_palabras.get(palabra, 0) + 1

print("Cantidad de apariciones por palabra:")
print(cantidad_palabras)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

for i in range(3):
    alumno = input("Ingrese el nombre del alumno: ")
    notas_str = input("Ingrese sus 3 notas separadas por comas: ")
    
    notas = tuple(map(int, notas_str.split(",")))
    
    promedio = sum(notas) / len(notas)
    
    print(f"El promedio de {alumno} es: {promedio:.2f}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {1, 2, 3, 4, 13, 7, 8, 9, 15, 11}
parcial2 = {9, 1, 10, 8, 13, 6, 8, 9, 3, 2}

ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

productos = {
    "arroz": 10,
    "fideos": 5,
    "chocolate": 14,
    "leche": 3,
    "pan lactal": 5,
    "aceite": 6,
    "manteca": 8,
    "harina": 10    
}

producto = input("Ingrese el nombre del producto: ").lower()

if producto in productos:
    print(f"Stock actual de '{producto}': {productos[producto]}")
    cantidad = int(input("¿Cuántas unidades desea agregar? "))
    productos[producto] += cantidad
    print(f"Nuevo stock de '{producto}': {productos[producto]}")
else:
    cantidad = int(input(f"'{producto}' no existe. ¿Cuántas unidades desea agregar como nuevo producto? "))
    productos[producto] = cantidad
    print(f"Producto '{producto}' agregado con stock de {cantidad} unidades.")

print("\nStock actualizado:")
print(productos)

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("lunes", "09:00") : "Reunión", 
    ("martes", "12:00") : "Ir al doctor", 
    ("miércoles", "11:00") : "Pilates",
    ("jueves", "17:00") : "Sesión con el psicólogo",
    ("viernes", "11:00") : "Pilates",
}

dia = input("Ingrese el día: ").lower()
hora = input("Ingrese la hora (formato HH:MM): ")

clave = (dia, hora)

if clave in agenda:
    print(f"La actividad del {dia.capitalize()} a las {hora} es: {agenda[clave]}")
else:
    print("No hay actividad registrada en ese día y horario.")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Japón": "Tokio",
    "Brasil": "Brasilia",
    "Italia": "Roma"
}

capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print(capitales_paises)