#EJERCICIO 1

#Función para leer 3 tanques de combustible y muestre el promedio
from cmath import tan
from itertools import count

count = 0


def combustible_informe(uno, dos, tres):
    print(f'Combustible Tanque1: {uno} Tanque2: {dos} Tanque3: {tres}')
    return 'Combustible Tanque1: {uno} Tanque2: {dos} Tanque3: {tres}'

combustible_informe(6,590,653)

# Función promedio
def combustible_promedio(total, tanques):
    total += total
    print(f'Promedio {total/tanques}')
    return total/tanques

combustible_promedio(1000, 3)

# Actualiza la función
def combustible_informe(uno, dos, tres):    
    print(f'Combustible Tanque1: {uno} Tanque2: {dos} Tanque3: {tres}')
    print(f'Combustible Promedio {combustible_promedio((uno+dos+tres), 3)}')
    return 'Combustible Tanque1: {uno} Tanque2: {dos} Tanque3: {tres}, Promedio: {combustible_promedio((uno+dos+tres), 3)}'

combustible_informe(100,0,6953)

#EJERCICIO 2
# Función con un informe preciso de la misión. Considera hora de prelanzamiento, tiempo de vuelo, destino, tanque externo y tanque interno
def mision(prelanzamiento, tiempo_vuelo, destino, tanque_ext, tanque_int):
    print(
        f'prelanzamiento: {prelanzamiento}, tiempo_vuelo: {tiempo_vuelo}, destino: {destino}, tanque_ext: {tanque_ext}, tanque_int: {tanque_int}')


mision(10, 10, 'Luna', 500, 20)

# Escribe tu nueva función de reporte
def mision_2(prelanzamiento, tiempo_vuelo, destino, **tanques):
    tanque = ''
    for item in tanques:
        tanque += f'{item}={tanques[item]} '
    print(f'prelanzamiento: {prelanzamiento}, tiempo_vuelo: {tiempo_vuelo}, destino: {destino}, Tanques: {tanque}')
    


mision_2(10, 10, 'Luna', tanque1=500, tanque2=100, tanque3=1000)

