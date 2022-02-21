#Ejercicio 1

from math import floor

tierra = 149597870
jupiter = 778547200

#km - Millas
distancia = abs(tierra - jupiter)
print(distancia)  # 628949360

distancia_millas = floor(distancia*0.621)
print(distancia_millas) # 390577552

#----------------------------
#Ejercicio 2
planeta_1 = int(input("¿Cuál es la distancia del primer planeta?"))
planeta_2 = int(input("¿Cuál es la distancia del segundo planeta?"))
#print(planeta_1, planeta_2)

resultado = abs(planeta_1 + planeta_2)
print(resultado)

resultado_millas = floor(resultado*0.621)
print(resultado_millas)

#Mercurio	57900000
#Venus	108200000
#Tierra	149600000
#Marte	227900000
#Júpiter	778600000
#Saturno	1433500000
#Urano	2872500000
#Neptuno	4495100000