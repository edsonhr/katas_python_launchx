# Ejercicio 1 - Creación de diccionarios de Python

print("\nEjercicio 1\n")

# Crea un diccionario llamado planet con los datos propuestos
planet = {
    'name': 'Mars',
    'moons': 2
}

# Muestra el nombre del planeta y el número de lunas que tiene.
print(f'{planet["name"]} tiene {planet["moons"]} lunas.')

# Agrega la clave circunferencia con los datos proporcionados previamente
planet['circunferencia (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}

# Imprime el nombre del planeta con su circunferencia polar.
print(f'{planet["name"]} tiene una circunferencia polar de {planet["circunferencia (km)"]["polar"]}')

# Ejercicio 2 - Programación dinámica con diccionarios

print("\nEjercicio 2\n")

# Planets and moons

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

# Añade el código para determinar el número de lunas.

# Obtenemos la lista de las lunas
# Almacenamos los resultados en una variable moons
moons = planet_moons.values()
print(f'El número de lunas de cada planeta es {moons}')

# Obtenemos el total de planetas
# Almacenamos los resultados en una variable llamada years
planets = len(planet_moons.keys())
print(f'El número total de planetas es {planets}')

# Calcula el total_moons agregando todas las lunas
# Almacena su valor en una variable llamada total_moons

total_moons = 0
for i in moons:
    total_moons = total_moons + i

# Calcula el promedio dividiendo el total_moons por el número de planetas
promedio = total_moons / planets

# Muestra el promedio
print(f'El promedio de lunas es {promedio}')