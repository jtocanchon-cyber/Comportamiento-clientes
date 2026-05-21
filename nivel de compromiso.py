# ###########################################
# Nombre:John Fredy Tocanchon Castañeda
# Codigo:1073606639
# Fundamentos de programación
# grupo:  213022_824
#############################################

# Matriz de datos: [ID Cliente, Duración (segundos), Eventos Clics]
sesiones = [
    ["C001", 240, 12],
    ["C002", 45, 2],
    ["C003", 120, 5],
    ["C004", 200, 7],
    ["C005", 80, 10]
]

# Módulo para calcular la clasificación de compromiso
def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

# Generación del informe
print("=== Informe de Compromiso de Sesiones ===")

for sesion in sesiones:
    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print(f"Cliente: {id_cliente} -> Compromiso: {clasificacion}")