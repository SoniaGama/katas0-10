
planets = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune']

print('The first planet is', planets[0])
print('The second planet is', planets[1])
print('The third planet is', planets[2])

planets[3] = 'Red Planet'
print('Mars is also known as', planets[3])

number_of_planets = len(planets)
print('There are', number_of_planets, 'planets in the solar system.')

#Para agregar un elemento a una lista append()
#longitud len()
planets.append('Pluto')
number_of_planets = len(planets)
print('There are actually', number_of_planets, 'planets in the solar system.')

#Eliminar valores de una lista, ultimo elemento pop()
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print('No, there are definitely', number_of_planets, 'planets in the solar system.')

print("The first planet is", planets[0])

#Índices negativos
#Los índices comienzan en cero y aumentan. 
# Los índices negativos comienzan al final de la lista y trabajan hacia atrás.
print('The last planet is', planets[-1])
print('The penultimate planet is', planets[-2])

#Buscar un valor en una lista index()
#busca el valor y devuelve el índice de ese elemento en la lista. 
# Si no encuentra una coincidencia, devuelve -1.
jupiter_index = planets.index('Jupiter')
print('Jupiter is the', jupiter_index + 1, 'planet from the sun')

gravity_on_earth = 1.0
gravity_on_the_moon = 0.166

gravity_on_planets = [0.378, 0.907, 1, 0.379, 2.36, 0.916, 0.889, 1.12]

#calcular el peso de un bus de dos pisos
bus_weight = 12650  # in kilograms, on Earth
print('On Earth, a double-decker bus weighs', bus_weight, 'kg')
print('On Mercury, a double-decker bus weighs', bus_weight * gravity_on_planets[0], 'kg')

#min() y max () con listas
print(min(gravity_on_planets))
print(max(gravity_on_planets))

#calcula los pesos mínimos y máximos en el sistema solar del bus
bus_weight = 12650  # in kilograms, on Earth
print('On Earth, a double-decker bus weighs', bus_weight, 'kg')
print('The lightest a bus would be in the solar system is',
      bus_weight * min(gravity_on_planets), 'kg')
print('The heaviest a bus would be in the solar system is',
      bus_weight * max(gravity_on_planets), 'kg')


#Slice , tiene los índices inicial y final de los elementos que queremos recuperar.
#se crea una nueva lista
#La Tierra es la tercera en la lista. Para obtener los planetas antes que la Tierra, use un slice
planets = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets_before_earth = planets[0:2]
print(planets_before_earth)

planets_after_earth = planets[3:8]
print(planets_after_earth)

#Si no coloca el índice de detención en el slice, 
# Python asume que deseas ir al final de la lista:
planets_after_earth = planets[3:]
print(planets_after_earth)

#Uniendo listas
#Para unir dos listas, utilice el operador (+)

#Crea dos listas. Llene la primera lista con las cuatro lunas de 
# Amaltea y la segunda lista con las cuatro lunas galileanas. 
# Únelos para crear una nueva lista:
amalthea_group = ['Metis', 'Adrastea', 'Amalthea', 'Thebe']
galilean_moons = ['Io', 'Europa', 'Ganymede', 'Callisto']

regular_satellite_moons = amalthea_group + galilean_moons
print('The regular satellite moons of Jupiter are', regular_satellite_moons)

#Ordenar listas sort()
#ista de cadenas en orden alfabético
#lista de números en orden numérico
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
#['Adrastea', 'Amalthea', 'Callisto', 'Europa', 'Ganymede', 'Io', 'Metis', 'Thebe']

#Ordenar en reversa .sort(reverse=True)
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
#.sort modifica la lista actual


