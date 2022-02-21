# EJERCICIO 1
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

# Ciclo para cambiar C a Celsius

# Dividir el texto en cada oracion
text.split('.')
text.lower().split('.')


# Define las palabras pista: average, temperature y distance suenan bien
#average, temperature y distance
word_1 = 'average'
word_2 = 'temperature'
word_3 = 'distance'

# Ciclo for para recorrer la cadena, imprimir datos relacionados con las palabras clave
count_1 = 0
count_2 = 0
count_3 = 0

for item in text.lower().split('.'):
    if word_1 in item:
        count_1 +=1
        print(f'"{word_1}" found {count_1} times. Item: {item.title()}')
    elif word_2 in item:
        count_2 +=1
        print(f'"{word_2}" found {count_2} times. Item: {item.title()}')
    elif word_3 in item:
        count_3 += 1
        print(f'"{word_3}" found {count_3} times. Item: {item.title()}')

# Ciclo para cambiar C a Celsius
for item in text.split('.'):
    if item.endswith('C'):
        item_repl = item.replace('C', 'Celsius')
        print(item_repl)

#---------------------------------
# EJERCICIO 2

#Gravity Facts about Ganymede
#-------------------------------------------------------------------------------
#Planet Name: Mars
#Gravity on Ganymede: 1.4300000000000002 m/s2

# Datos con los que vas a trabajar
name = "Moon"
gravity = 0.00162*1000  # in kms
planet = "Earth"

#Gravity Facts about Moon
# Primero, crea un título para el texto. Utiliza las variables en lugar de escribir.

#Ahora crea una plantilla de cadena multilínea para contener el resto de la información.
#En lugar de usar kilómetros, debes convertir la distancia a metros multiplicando por 1, 000.

title = f'gravity facts about {name}'.title()

#title_pl = f'{title_planet.title()}'
#planet_name = f'Planet Name: {planet}'
#gravity_planet = f'Gravity on Ganymede: {g_planet} m/s2'

template = f'{title}\nPlanet Name: {planet}\nGravity on {name}: {gravity} m/s2'
print(template)

planet = 'Marte '
gravity = 0.00143*1000
name = 'Ganímedes'
title = f'gravity facts about {name}'.title()

#template = '{title}\nPlanet Name: {planet}\nGravity on {name}: {gravity} m/s2'.format(title=title, planet=planet,name=name, gravity=gravity)
template = '{title}\nPlanet Name: {planet}\nGravity on {name}: {gravity} m/s2'

print(template.format(title=title, planet=planet, name=name, gravity=gravity))

#template = f'{title}\nPlanet Name: {planet}\nGravity on {name}: {gravity} m/s2'
#print(template)


planet = 'Jupiter '
gravity = 0.00200*1000
name = 'Luna'
title = f'gravity facts about {name}'.title()

print(template.format(title=title, planet=planet, name=name, gravity=gravity))

