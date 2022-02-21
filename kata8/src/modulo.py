#Diccionario
#colección de pares clave-valor
planet = {
    'name': 'Earth',
    'moons': 1
}

print(planet.get('name'))  # Earth

# planet['name'] es idéntico a usar planet.get('name')
print(planet['name'])  # Earth

# Si una clave no está disponible:
# get devuelve None
# [ ] genera un error KeyError.

wibble = planet.get('wibble')  # Regresa None
#wibble = planet['wibble']  # KeyError: 'wibble'

#Modificación de valores de un diccionario
planet.update({'name': 'Makemake'}) # name ahora es Makemake

planet['name'] = 'Makemake' # name is now set to Makemake

# Usando update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Usando corchetes
planet['name'] = 'Jupiter'
planet['moons'] = 79

print(planet['name'], planet['moons'])

planet['orbital period'] = 4333

# Actualizar planet para incluir el período orbital en días:

# el diccionario planet ahora contiene: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }


# Eliminar clave pop
planet.pop('orbital period')

# el diccionario planet ahora contiene: {
#   name: 'jupiter'
#   moons: 79
# }

# Debes que almacenar el diámetro de planet

# Añadimos los datos
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# el diccionario planet ahora contiene: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }

print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')
# Salida: Jupiter polar diameter: 133709

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

print(rainfall.keys(), 'Keys')
#dict_keys(['october', 'november', 'december']) Keys
#keys() regresa una lista con todas las keys

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

# Salida:
# october: 3.5cm
# november: 4.2cm
# december: 2.1cm

#agregar un valor en lugar de sobrescribirlo
# El valor de december: 2.1cm
# Si, 'december' existe en rainfall
if 'december' in rainfall:
    # rainfall [en la posición december] es igual a
    # rainfall [en la posición december] + 1 (2.1+1)
    rainfall['december'] = rainfall['december'] + 1

# Si no:
else:

    # rainfall [en la posición december] es igual a 1
    rainfall['december'] = 1

# Como december si existe, el valor será 3.1


#values() lista de los valores sin claves
#Total de precipitaciones 0
total_rainfall = 0
print(rainfall.values(), 'Values')

# Para cada valor en los valores de rainfall
for value in rainfall.values():

    # El total de las precipitaciones será igual a ese mismo + el valor que se está iterando
    #print(value, 'Value')
    total_rainfall = total_rainfall + value

# Muestra 'Hay un total de precipitaciones (el valor total) en centímetros en el último cuarto (haciendo referencia al cuarto del año)

print(f'There was {total_rainfall}cm in the last quarter')

# Salida:
# There was 10.8cm in the last quarter
