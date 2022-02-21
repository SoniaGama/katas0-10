fact = 'The Moon has no atmosphere.'
fact + 'No sound can be heard on the Moon.'
two_facts = fact + 'No sound can be heard on the Moon.'


print(two_facts)

multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

multiline2 = """Facts about the Moon:
...  There is no atmosphere.
...  There is no sound."""
print(multiline2)

'temperatures and facts about the moon'.title()

heading = 'temperatures and facts about the moon'
print(heading.title())
#Temperatures And Facts About The Moon

# split() convierte una cadena en un array o lista.
# cada elemento es separado por un espacio
temperatures = '''Daylight: 260 F
... Nighttime: -280 F'''
print(temperatures.split())
#['Daylight:', '260', 'F', '...', 'Nighttime:', '-280', 'F']

print(temperatures.split('\n'))
#['Daylight: 260 F', '... Nighttime: -280 F']

print('Moon' in 'This text will describe facts and challenges with space travel')
#False

print('Moon' in 'This text will describe facts about the Moon')
#Salida: True

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""

print(temperatures.find('Moon')) #-1

#find() Deuelve la posición de una cadena o  -1 si no lo encuentra

print(temperatures.find('Mars')) #68

#.count() Devuelve el número total de apariciones de palabra en una cadena
print(temperatures.count('Mars')) #1
print(temperatures.count('Moon')) #0

print("The Moon And The Earth".lower())  # the moon and the earth
print('The Moon And The Earth'.upper()) #THE MOON AND THE EARTH

temperatures = 'Mars Average Temperature: -60 C'
parts = temperatures.split(':')
print(parts)
#Salida: ['Mars average temperature', ' -60 C']

print(parts[-1])  # -60 C

mars_temperature = 'The highest temperature on Mars is about 30 C'

for item in mars_temperature.split():
    if item.isnumeric():
        print(item) #30

# .isdecimal()
# .isnumeric()
# .startswith() Para numeros negativos que empiezan con -
# .endswith() En que termina

print('-60'.startswith('-')) #true

if "30 C".endswith("C"):
    print("This temperature is in Celsius")

cda_1 = 'Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.'
cda_2 = cda_1.replace('Celsius', 'C')

print(cda_2)
#'Saturn has a daytime temperature of -170 degrees C, while Mars has -28 C.'

text = 'Temperatures on the Moon can vary wildly.'
print('temperatures' in text) # False
print('temperatures' in text.lower()) #True

moon_facts = ['The Moon is drifting away from the Earth.', 'On average, the Moon is moving about 4cm every year']
print('\n'.join(moon_facts))

# join une los elementos de una lista
# \n elemento para unir

#INTERPOLACION

mass_percentage = '1/6'
#On the Moon, you would weigh about 1/6 of your weight on Earth
print('On the Moon, you would weigh about %s of your weight on Earth' %mass_percentage)
# El marcador de posición es %s, y la variable se pasa al texto después del carácter % fuera de la cadena

print("""Both sides of the %s get the same amount of sunlight,
    but only one side is seen from %s because
    the %s rotates around its own axis when it orbits %s.""" %('Moon', 'Earth', 'Moon', 'Earth'))
#Both sides of the Moon get the same amount of sunlight, but only one side is seen from Earth because the Moon rotates around its own axis when it orbits Earth.

mass_percentage = '1/6'
print('On the Moon, you would weigh about {} of your weight on Earth'.format(mass_percentage))

#asigación por indice
print("""You are lighter on the {0}, because on the {0} 
... you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))

#asignación por palabras clave
print("""You are lighter on the {moon}, because on the {moon} 
... you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))

#f-strings cadenas plantillas para interpolar directamente una variable
print(f'On the Moon, you would weigh about {mass_percentage} of your weight on Earth')

print(round(100/6, 1)) #porcentaje de 1/6

print(f'On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth')

subject = 'interesting facts about the moon'
print(f'{subject.title()}')
