
#    Create an empty dictionary called dog
dog={}

#    Add name, color, breed, legs, age to the dog dictionary
dog={'name':'dog_name','color':'dog_color','legs':'dog_legs','age':'dog_age'}

#    Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
estudiante={
    'nombre':'Jorge',
    'apellido':'Lutz',
    'sexo':'Hombre',
    'edad':'25',
    'estado_civil':'soltero',
    'habilidades':['python','ingles'],
    'pais': 'Chile',
    'ciudad':'Coquimbo',
    'direccion':'Avenida azul'
}

#    Get the length of the student dictionary
print(len(estudiante))

#    Get the value of skills and check the data type, it should be a list
print(type(estudiante['habilidades']))

#    Modify the skills values by adding one or two skills
estudiante['habilidades'].append('javascript')
print(estudiante['habilidades'])

#    Get the dictionary keys as a list
keys=estudiante.keys()
print(keys)

#    Get the dictionary values as a list
values=estudiante.values()
print(values)

#    Change the dictionary to a list of tuples using items() method
print(estudiante.items())

#    Delete one of the items in the dictionary
del estudiante['direccion']
print(estudiante)

#    Delete one of the dictionaries
del estudiante
print(estudiante)

