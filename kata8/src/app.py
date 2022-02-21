# EJERCICIO 1
#Diccionario planet
planet ={
    'name': 'Mars',
    'moons': 2
}

# Muestra el nombre del planeta y el número de lunas que tiene.
print(f"Planeta: {planet['name']} Lunas:{planet.get('moons')}")

#Actualizar claves existentes
planet['circunfetencia(km)'] = {
    'polar': 6752,
    'equatorial': 6792
}
#print((planet.get('circunfetencia(km)'))['polar'])
#print(((planet['circunfetencia(km)']))['polar'])

#(planet.get('circunfetencia(km)'))['polar']
#((planet['circunfetencia(km)']))['polar']

# Imprime el nombre del planeta con su circunferencia polar.
print(f"Planeta {planet['name']} Circunferencia Polar {((planet['circunfetencia(km)']))['polar']}")
#Solucion
#print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')

for key in planet:
    if key == 'circunfetencia(km)':
        print(f"Planet: {planet['name']} Circunferencia Polar: {planet[key].get('polar')}")


#EJERCICIO 2
# Planets and moons
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

# Añade el código para determinar el número de lunas.
planets = planet_moons.keys()
moons = planet_moons.values()

#total de lunas y promedio
moon = 0
for i in moons:
    moon += i

#promedio = moon/len(planets)
print(f'Total de Lunas {moon}, Promedio de lunas {moon/len(planets)}')



