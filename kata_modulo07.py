# Ejercicio 1
print("\nEjercicio 1\n")

# Declaramos 2 variables
new_planet = ''
planets = []

# Escribe el ciclo while solicitado
while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
        print(planets) #Imprimo el contenido de mi lista cada vez que se agrega un planeta
    new_planet = input('Ingresa un planeta ')


# Ejercicio 2
print("\nEjercicio 2\n")

# Escribe tu ciclo for para iterar en una lista de planetas
print('Contenido de mi lista de planetas')
for i in planets:
    print(i)