from datetime import timedelta, datetime

#Funciones sin argumentos
# Defino mi función
def rocket_parts():
    print('payload, propellant, structure')

# Llamo a mi función
rocket_parts()
#'payload, propellant, structure'

output = rocket_parts()
#output is None - no tiene return
#True

def rocket_parts():
    return 'payload, propellant, structure'


#>> > any([True, False, False])
#True
#>> > any([False, False, False])
#False

#>> > any()
#Traceback(most recent call last):
#  File '<stdin>', line 1, in <module >
#TypeError: any() takes exactly one argument(0 given)

#>> > str()
#'' devuelve una cadena vacía:
#>> > str(15)
#'15'


#Exigencia de un argumento
def distance_from_earth(destination):
    if destination == 'Moon':

        return '238,855'
    else:
        return 'Unable to compute to that destination'

print(distance_from_earth('Moon')) #'238,855'
print(distance_from_earth('Marte'))  # '238,855'

#Varios argumentos necesarios
def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

print(days_to_complete(238855, 75))

#Funciones como argumentos
total_days = days_to_complete(238855, 75)
print(round(total_days)) # 133

print(round(days_to_complete(238855, 75)))

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime('Arrival: %A %H:%M')

print(arrival_time()) #'Arrival: Saturday 16:42'
print(arrival_time(hours=0))  # Arrival: Monday 00:20


#Combinación de argumentos y argumentos de palabra clave
#Los argumentos siempre se declaran primero, 
# seguidos de argumentos de palabra clave.
def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f'{destination} Arrival: %A %H:%M')

print(arrival_time('Moon'))
print(arrival_time('Orbit', hours=0.13))

#Argumentos de variable
# la función permite pasar cualquier número de argumentos 0...
def variable_length(*args):
    print(args)

variable_length()
variable_length('one', 'two')

# función de longitud variable que pueda calcular cuántos minutos quedan hasta el inicio
def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f'Total time to launch is {total_minutes} minutes'
    else:
        return f'Total time to launch is {total_minutes/60} hours'


print(sequence_time(4, 14, 18))
print(sequence_time(4, 14, 48))

# *args no se le asigna un nombre de variable
# **kwargs acepte cualquier número de argumentos de palabra clave
def variable_length(**kwargs):
    print(kwargs)


variable_length(tanks=1, day='Wednesday', pilots=3)
# Los argumentos de palabra clave de longitud variable 
# se asignan como un diccionario


def crew_members(**kwargs):
    print(f'{len(kwargs)} astronauts assigned for this mission:')
    for title, name in kwargs.items():
        print(f'{title}: {name}')


crew_members(captain='Neil Armstrong', pilot='Buzz Aldrin',
             command_pilot='Michael Collins')

#Las palabras clave repetidas producirán un error


