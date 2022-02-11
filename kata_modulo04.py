#Ejercicio 1

print("\nEjercicio 1")

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
print(f'\n\nTexto original: \n{text}\n')

#Primero, divide el texto en cada oración para trabajar con su contenido
texto_div = text.split('.')
print(f'Este es el texto dividido: \n{texto_div}\n')

#Define las palabras pista: average, temperature y distance suenan bien
palabras_clave = ["average", "temperature", "distance"]
print(f'Palabras clave que voy a buscar en cada oración {palabras_clave}\n')

# Ciclo for para recorrer la cadena
print('Este es el resultado de la búsqueda:')
for oracion in texto_div:
    for palabra_clave in palabras_clave:
        if palabra_clave in oracion:
            print(oracion)

# Ciclo para cambiar C a Celsius
print('\nEste es el resultado de reemplazar C por Celsius:')
for oracion in texto_div:
    for palabra_clave in palabras_clave:
        if palabra_clave in oracion:
            print(oracion.replace(' C', ' Celsius'))

#Ejercicio 2

print("\nEjercicio 2\n\n")

# Datos con los que vas a trabajar
nombre = "Moon"
gravedad = 0.00162 # in kms
planeta = "Earth"

# Creando el título
title = f'Información de gravedad sobre {nombre}'

# Creando la plantilla
informacion = f"""{'-'*80} 
Nombre del planeta: {planeta} 
Gravedad en {nombre}: {gravedad * 1000} m/s2 
"""

# Unión de ambas cadenas
plantilla = f"""{title.title()} 
{informacion} 
""" 
print(plantilla)

# Nuevos datos muestra con Marte
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'

print(plantilla)

#Nueva plantilla con .format
nueva_plantilla = """
Información de gravedad sobre: {nombre}
-------------------------------------------------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""
print(nueva_plantilla.format(nombre=nombre, planeta=planeta, gravedad=gravedad))

# Imprimiendo resultado
print(nueva_plantilla.format(nombre=nombre, planeta=planeta, gravedad=gravedad*1000))