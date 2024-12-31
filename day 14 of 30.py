from functools import reduce
from countries_data import paises
#---Exercises LVL1

#Explain the difference between map, filter, and reduce.
"""
Son funciones de alto orden en python que tienen utilidades distintas, si bien las 3 son iterativas, es decir, recorren una lista, tienen
objetivos distintos.
map() itera una lista dada y aplica un metodo(def) dado tambien, a todos los elementos de la lista.
filter() itera una lista dada a traves de un metodo(def) y discrimina entre true or false, por lo que se ha de establecer un criterio
condicional con result true or false.
reduce() itera una lista dada y lo corre a traves de un metodo(def) dado, pero retorna un valor unico y no una lista como las anteriores 
"""

#Explain the difference between higher order function, closure and decorator
"""
Las funciones de alto orden son metodos(def), que son capaces capaces de entregar otros metodos(def) como resultado.

un decorador es una funcion de alto orden que permite modificar el resultado de la funcion sin modificar su estructura, es decir, se añade
un tinte a una tela. La tela sigue funcionando como tela pero ahora posee un color.(por ejemplo capitalize()el resuldato de un metodos(def))

Enclosure es la concatenacion de un metodos(def) dentro de otro metodos(def), permitiendo la ejecucion de ambos metodos(def) con solo llamar
al contenedor
"""

#Define a call function before map, filter or reduce, see examples.
"""
persons=['house','amber','chase','foreman','wilson','cameron']
def greet(p):
    
    return 'Hola {}, como estas?'.format(p)
greeting=map(greet, persons)
print(list(greeting))
"""

#Use for loop to print each country in the countries list.
paises
def enumeracion_paises(p):
    return 'Pais {}'.format(p)
numero_pais= map(enumeracion_paises, paises)
for pais in numero_pais:
    print(pais)
#Use for to print each name in the names list.


#Use for to print each number in the numberslis


#---Exercises LVL2


#Use map to create a new list by changing each country to uppercase in the countries list

#Use map to create a new list by changing each number to its square in the numbers list

#Use map to change each name to uppercase in the names list

#Use filter to filter out countries containing 'land'.

#Use filter to filter out countries having exactly six characters.

#Use filter to filter out countries containing six letters and more in the country list.

#Use filter to filter out countries starting with an 'E'

#Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

#Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

#Use reduce to sum all the numbers in the numbers list.

#Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

#Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

#Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.

#Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.

#Declare a get_last_ten_countries function that returns the last ten countries in the countries list.


#--Excercises LVL3

#Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:

#Sort countries by name, by capital, by population

#Sort out the ten most spoken languages by location.

#Sort out the ten most populated countries.

