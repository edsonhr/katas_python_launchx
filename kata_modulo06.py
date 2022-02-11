# Ejercicio 1
# Creamos la lista planets y la mostramos

print("\nEjercicio 1\n")

planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']

print(f'Los planetas del sistema solar son {planetas}')

# Agregamos a plutón y mostramos el último elemento
planetas.append('Plutón')
print(planetas[-1], 'es el último planeta del sistema solar.')

# Ejercicio 2
print("\nEjercicio 2\n")

# Lista de planetas
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

# Solicitamos el nombre de un planeta *Pista:  input()*
planeta_buscar = input('Ingrese en nombre del planeta respetando la primer letra en mayúscula) ')

# Busca el planeta en la lista
busqueda = planets.index(planeta_buscar)

# Muestra los planetas más cercanos al sol
print('Estos son los planetas más cercanos a ' + planeta_buscar)
print(planets[0:busqueda])

# Muestra los planetas más lejanos al sol
print('Estos son los planetas más lejanos a ' + planeta_buscar)
print(planets[busqueda + 1:])


