from functools import reduce
from countries import countriess
from countries_data import paises
from collections import Counter
#--Resources
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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
"""
x=0
for i in countries:
    print(countries[x])
    x+=1
"""

#Use for to print each name in the names list.
"""
x=0
for i in names:
    print(names[x])
    x+=1
"""

#Use for to print each number in the numberslis
"""
x=0
for i in numbers:
    print(numbers[x])
    x+=1
"""

#---Exercises LVL2


#Use map to create a new list by changing each country to uppercase in the countries list
"""
def string_upper(c):
    return c.upper()

upper_country=map(string_upper,countries)
print(list(upper_country))
"""

#Use map to create a new list by changing each number to its square in the numbers list
"""
def cuadratura(n):
    return n**2
numero_cuadrado=map(cuadratura,numbers)
print(list(numero_cuadrado))
"""

#Use map to change each name to uppercase in the names list
"""
def string_upper(n):
    return n.upper()

upper_name=map(string_upper,names)
print(list(upper_name))
"""

#Use filter to filter out countries containing 'land'.
"""
def coincidence_checker(c):    
    if 'land' in c:
        return False
    return True
land_filter=filter(coincidence_checker,countries)
print(list(land_filter))
"""

#Use filter to filter out countries having exactly six characters.
"""
def country_counter(c):
    if len(c)==6:
        return False
    return True
count_filter=filter(country_counter, countries)
print(list(count_filter))
"""

#Use filter to filter out countries containing six letters and more in the country list.
"""
def country_counter(c):
    if len(c)>6:
        return False
    return True
count_filter=filter(country_counter, countries)
print(list(count_filter))
"""

#Use filter to filter out countries starting with an 'E'
"""
def e_checker(c):
    if 'E'==c[0]:
        return False
    return True
e_filter=filter(e_checker,countries)
print(list(e_filter))
"""

#Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
"""
cadena= reduce(lambda x,y:x+y,filter(lambda x : x % 2==0, numbers))
print(cadena)
"""

#Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
"""
def get_string_lists(s):
    return str(s)
string_list=map(get_string_lists,numbers)
print(list(string_list))
"""

#Use reduce to sum all the numbers in the numbers list.
"""
suma_reducida=reduce(lambda x,y:x+y, numbers)
print(suma_reducida)
"""

#Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
"""
def sentence(x,y):
    return x+' '+y
concatenacion=reduce(sentence, countries)
print(concatenacion)
"""

#Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
"""
def categorize_counties(c):
    if 'land'in c:
        return True
    return False
categoria=filter(categorize_counties,countriess)
print(list(categoria))
"""

#Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
"""
def dicc_count(countries):
    letter_count={}
    for country in countries:
        first_letter=country[0].upper()
        if first_letter in letter_count:
            letter_count[first_letter]+=1
        else:
            letter_count[first_letter] = 1
    return letter_count
result=dicc_count(countries)
print(result)
"""

#Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
"""
def country_getter(countriess):
    first_ten=[]
    i=0
    while i<10:
        first_ten.append(countriess[i])
        i+=1
    return first_ten
diez=country_getter(countriess)
print(diez)
"""

#Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
"""
def country_getter(countriess):
    last_ten=[]
    i=0
    countriess.reverse()
    while i<10:
        last_ten.append(countriess[i])
        i+=1
    return last_ten
diez=country_getter(countriess)
print(diez)
"""

#--Excercises LVL3

#Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:

#Sort countries by name, by capital, by population
"""
def name_getter(country):
    return country["name"]

nombres_paises=map(name_getter,paises)
nombres_ordenados=sorted(list(nombres_paises))
print(list(nombres_ordenados))
"""

"""
def capital_getter(country):
    return country["capital"]

capital_paises = map(capital_getter, paises)
capitales_ordenadas = sorted(list(capital_paises))
print(capitales_ordenadas)
"""
"""
def poblacion_getter(country):
    return country['population']

poblacion_paises=map(poblacion_getter,paises)
poblacion_ordenado= sorted(list(poblacion_paises), reverse= True)
print(poblacion_ordenado)
"""

#Sort out the ten most spoken languages by location.
"""
n=10
contador_idiomas = Counter()
for pais in paises:
    idiomas = pais.get('languages', [])
    contador_idiomas.update(idiomas)
idiomas_mas_comunes = contador_idiomas.most_common(n)
top_10_idiomas=idiomas_mas_comunes
for idioma, frecuencia in top_10_idiomas:
    print(f"{idioma}: hablado en {frecuencia} países")
"""

    
#Sort out the ten most populated countries.
"""
def encontrar_paises_mas_poblados(paises, n=10):
    paises_ordenados = sorted(paises, key=lambda x: x.get('population', 0), reverse=True)
    top_n_paises = paises_ordenados[:n]
    return top_n_paises
top_10_paises = encontrar_paises_mas_poblados(paises, 10)
print("Los 10 países con mayor población son:")
for i, pais in enumerate(top_10_paises, 1):
    nombre = pais.get('name', 'Desconocido')
    poblacion = pais.get('population', 'Desconocida')
    print(f"{i}. {nombre}: {poblacion:,} habitantes")
"""

