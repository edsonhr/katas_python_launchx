# Ejercicio 1 - if, else
print('\nEjercicio 1')

vel_asteroide = 49

if vel_asteroide > 25:
    print('¡Alerta - Un asteroide se está acercando a la Tierra!')
else:
    print('Sin peligro')

#Ejercicio 2 - if, else, y elif
print('\nEjercicio 2')

vel_asteroide = 19

if vel_asteroide > 20:
    print('¡Mira hacia el cielo, es un asteroide!')
elif vel_asteroide == 20:
    print('¡Mira hacia el cielo, es un asteroide!')
else:
    print('No hay nada interesante en el cielo')


#Ejercicio 3 - Uso de operadores and y or
print('\nEjercicio 3')

vel_asteroide = 25
tam_asteroide = 40

if vel_asteroide > 25 and tam_asteroide > 25:
    print('¡Alerta - Un asteroide se está acercando a la Tierra!')
elif vel_asteroide >= 20:
    print('¡Mira hacia el cielo, es un asteroide!')
elif tam_asteroide < 25:
    print('No hay nada interesante en el cielo')
else:
    print('No hay nada interesante en el cielo')