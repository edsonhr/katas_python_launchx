# Ejercicio 1
# Crear variables para almacenar las dos distancias
# ¡Asegúrate de quitar las comas!

print("\nEjercicio 1\n")

planeta_1 = 149597870
planeta_2 = 778547200

# Calcular la distancia entre planetas

distancia = planeta_2 - planeta_1
print(f'La distancia en Kilometros entre los planetas es de {distancia}')

distancia_milla = distancia * 0.621
print(f'La distancia en Millas entre los planetas es de {distancia_milla}')

# Ejercicio 2
# Almacenar las entradas del usuario
# Pista: variable = input("¿Cuál es tu nombre?")

print("\nEjercicio 2\n")

planeta_1 = input('Introduzca la distancia del sol para el primer planeta en KM ')
planeta_2 = input('Introduzca la distancia desde el sol para el segundo planeta en KM ')

# Convierte las cadenas de ambos planetas a números enteros
planeta_1 = int(planeta_1)
planeta_2 = int(planeta_2)

# Realizar el cálculo y determinar el valor absoluto
distancia_km = planeta_2 - planeta_1
print(f'La distancia entre los planetas es de {abs(distancia_km)}')

# Convertir de KM a Millas
distance_milla = distancia_km * 0.621
print(f'La distancia en millas es de {distance_milla}')
