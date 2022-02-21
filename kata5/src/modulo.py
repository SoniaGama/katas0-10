from math import ceil, floor
#Biblioteca Math

answer = 30 + 12
print(answer)

difference = 30 - 12
print(difference)

product = 30 * 12
print(product)

quotient = 30 / 12
print(quotient)

#segundos en minutos
seconds = 1042
display_minutes = 1042 / 60
print(display_minutes)  # 17.366666666666667

#Siempre que desees redondear hacia abajo, utilizando lo que se conoce como división de piso. 
#Para realizar la división de piso en Python, utilizamos //
seconds = 1042
display_minutes = 1042 // 60
print(display_minutes) # 17

# El siguiente paso es determinar el número de segundos. 
# Este es el resto de si se divide por 1042. Puedes encontrar el resto utilizando el operador módulo
seconds = 1042
display_minutes = 1042 // 60
display_seconds = 1042 % 60

print(display_minutes)
print(display_seconds)

# Jerarquía de Operaciones
# 1.- Paréntesis
# 2.- Exponentes
# 3.- Multiplicación y división
# 4.- Suma y resta

result_1 = 1032 + 26 * 2
result_2 = 1032 + (26 * 2)
print(result_1, result_2)


#Convertir cadenas en números
demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

#Valores absolutos
#Un valor absoluto en matemáticas es el número no negativo sin su signo
print(abs(39 - 16))
print(abs(16 - 39))

#Redondeo
print(round(14.5))


#Biblioteca Math
round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)
