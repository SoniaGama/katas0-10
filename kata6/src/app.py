#Ejercicio 1
planets = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']

print(len(planets))

planets.append('Plutón')
print(len(planets))
print(planets[-1])

#Ejercicio 2
planets = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']
planeta_usuario = input('¿Nombre de planeta? Comience con mayuscula ' )

indice_planeta_usuario = planets.index(planeta_usuario)

#planetas mas cercanos al sol
planetas_mas_cercanos = planets[0:indice_planeta_usuario]
print(planetas_mas_cercanos)

#planetas mas alejados del sol
planetas_mas_lejanos = planets[indice_planeta_usuario+1:-1]
print(planetas_mas_lejanos)
