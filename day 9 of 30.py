#Exercises: Level 1

#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
"""
usuario_edad= input('Ingresa tu edad: ')
int_usuario_edad= int(usuario_edad)
if int_usuario_edad>18 :

    print('Tienes la edad suficiente para aprender a manejar')
if int_usuario_edad<18 :
    edad_faltante=18-int_usuario_edad
    print('No ienes la edad suficiente, intenta aprender en:',edad_faltante,'años más')
"""

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
"""
mi_edad=25
usuario_edad= input('Ingresa tu edad: ')
tu_edad=int(usuario_edad)
if mi_edad>tu_edad:
    diff_positiva=mi_edad-tu_edad
    if diff_positiva==1:
        print('Soy',diff_positiva,'año mas grande que tu')
    if diff_positiva>1:
        print('Soy',diff_positiva,'años mas grande que tu')
    else:
        print('...Que?')
if mi_edad<tu_edad:
    diff_negativa=tu_edad-mi_edad
    if diff_negativa==1:
        print('Eres',diff_negativa,'año mayor que yo')
    if diff_negativa>1:
        print('Eres',diff_negativa,'años mayor que yo')
    else:
        print('...Que?')
if mi_edad==tu_edad:
    print('BRIIIIGIIDOOOOOO')
"""

#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
"""
user_numero_a=input('Ingresa un numero: ')
user_numero_b=input('Ingresa un numero otra vez: ')
numero_a=int(user_numero_a)
numero_b=int(user_numero_b)

if numero_a>numero_b:
    print('El numero A es más grande que el numero B')
if numero_b<numero_a:
    print('El numero B es más grande que el numero A')
if numero_a==numero_b:
    print('... Ingresaste dos veces el mismo numero?')
else:
    print('... Que hiciste?')
"""
#Exercises: Level 2

#Write a code which gives grade to students according to theirs scores
"""
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""
"""
nota_alumno= input('Ingresa tu nota: ')
puntaje= int(nota_alumno)
if 0<=puntaje<50:
    print('Tu nota es "F"')
elif 49<puntaje<60:
    print('Tu nota es "D"')
elif 59<puntaje<70:
    print('Tu nota es "C"')
elif 69<puntaje<80:
    print('Tu nota es "B"')
elif 79<puntaje<101:
    print('Tu nota es "A"')
else:
    print('Ingresaste mal tu nota.')
"""

#Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
"""
mes_usuario=input('En que mes del año estas? ')
otoño=('septiembre','octubre','noviembre')
invierno=('diciembre','enero','febrero')
primavera=('marzo','abril','mayo')
verano=('junio','julio','agosto')
mes_user_low=mes_usuario.lower()
if mes_user_low in otoño:
    print('Estas en la estacion de otoño')
if mes_user_low in invierno:
    print('Estas en la estacion de invierno')
if mes_user_low in primavera:
    print('Estas en la estacion de primavera')
if mes_user_low in verano:
    print('Estas en la estacion de verano')
else:
    print('Ingresaste mal el mes')
"""

#The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
"""
user_fruta=input('Ingresa una fruta: ')
user_fruta_low=user_fruta.lower()
if user_fruta_low in fruits:
    print('Esta fruta ya existe!')
    print(fruits)
else:
    fruits.append(user_fruta_low)
    print('Hemos añadido tu fruta!')
    print(fruits)
"""

#Exercises: Level 3
#Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
# * If the person is married and if he lives in Finland, print the information in the following format:



