# Ejercicio 1
new_planet_input = ''
planets = []

while new_planet_input.lower() != 'done':
    if new_planet_input:
        planets.append(new_planet_input)
        #print(planets)
    new_planet_input = input('Nuevo valor, o done para finalizar ')

# Elercicio 2
# Crea un ciclo for para iterar sobre la lista planets
for planet in planets:
    print(f'Planeta {planet}')
