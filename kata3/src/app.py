# 1 velocidad
# 2 Luz
# 3 Tamaño - Multiples condiciones

# Ejericio 1 if else
velocidad_asteriode = 49

if velocidad_asteriode < 25:
    print("velocidad segura")
else:
    print("velocidad peligrosa")

# Ejercicio 2 if elif else --mayor o igual a 20km
velocidad_asteriode = 19

if velocidad_asteriode > 20:
    print("Miren al cielo veran un asteroide")
elif velocidad_asteriode == 20:
    print("Miren al cielo veran un asteroide")
else:
    print("No hay asteroides que sean visibles")

#Ejercicio 3
velocidad_asteriode = 25
tamaño_asteroide = 500

if velocidad_asteriode >= 20 and velocidad_asteriode < 25:
    print("Miren al cielo veran un asteroide.")
    if velocidad_asteriode < 25 and tamaño_asteroide < 25:
        print("Velocidad segura: " + str(velocidad_asteriode))
        print("Tamaño del asteroide: " + str(tamaño_asteroide) +" El asteroide se quemara en la atmosfera ")
elif velocidad_asteriode >= 25:
    print("Velocidad peligrosa: " + str(velocidad_asteriode))
    if tamaño_asteroide > 25 and tamaño_asteroide < 1000:
        print("Tamaño del asteroide: " + str(tamaño_asteroide) + ". Impactara la tierra")
elif velocidad_asteriode <=20:
    print("No hay asteroides que sean visibles")
else:
    print("No se han encontrado asteroides")