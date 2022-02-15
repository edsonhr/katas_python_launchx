# Ejercicio 1 - Uso de funciones en Python

print("\nEjercicio 1\n")

# Función para leer 3 tanques de combustible y muestre el promedio
def inf_combustible(t1, t2, t3):
    promedio = ((t1 + t2 + t3) / 3)
    return f"""Reporte:
    Promedio total: {promedio}%
    Tanque 1: {t1}%
    Tanque 2: {t2}%
    Tanque 3: {t3}% 
    """
# Llamamos a la función que genera el reporte print(funcion(tanque1, tanque2, tanque3))
print(inf_combustible(80, 70, 85))

# Función promedio 
def promedio(valores):
    total = sum(valores)
    numero_de_valores = len(valores)
    return total / numero_de_valores

# Imprimiendo el promedio
print (promedio([80, 70, 85]))

# Actualiza la función
def inf_combustible2(t1, t2, t3):
    return f"""Reporte completo:
    Promedio total: {promedio([t1, t2, t3])}%
    Tanque 1: {t1}%
    Tanque 2: {t2}%
    Tanque 3: {t3}% 
    """

# Pruebo nueva funcion modificada
print(inf_combustible2(80, 70, 85))

# Ejercicio 2 - Trabajo con argumentos de palabra clave

print("\nEjercicio 2")

# Función con un informe preciso de la misión. Considera hora de prelanzamiento, tiempo de vuelo, destino, tanque externo y tanque interno
def informe_preciso(hr_prelanzamiento, hr_vuelo, destino, t_externo, t_interno):
    return f"""
    Misión con destino a {destino}
    Tiempo total del viaje: {hr_prelanzamiento + hr_vuelo} minutos
    Combustible total: {t_externo + t_interno} galones
    """

print(informe_preciso(14, 51, "Moon", 200000, 300000))

# Escribe tu nueva función de reporte considerando lo anterior

def informe_preciso(destino, *minutos, **combustible):
    return f"""
    Misión con destino a {destino}
    Tiempo total del viaje: {sum(minutos)} minutos
    Combustible total: {sum(combustible.values())}
    """

print(informe_preciso("Moon", 10, 15, 51, main=300000, external=200000))

# Escribe tu nueva función

def informe_preciso(destino, *minutos, **combustible):
    informe = f"""
    Misión con destino a {destino}
    Tiempo total del viaje: {sum(minutos)} minutos
    Combustible total: {sum(combustible.values())}
    """
    for num_tanque, galones in combustible.items():
        informe += f"{num_tanque} tanque --> {galones} galones de reserva\n"
    return informe

print(informe_preciso("Moon", 8, 11, 55, Principal=300000, Secundario=200000))