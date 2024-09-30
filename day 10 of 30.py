from countries import countries
from countries_data import paises
from collections import Counter

#Exercises: Level 1

#Iterate 0 to 10 using for loop, do the same using while loop.
number=[0,1,2,3,4,5,6,7,8,9,10]
"""
number=[0,1,2,3,4,5,6,7,8,9,10]
for number in number:
    print('for number:',number)
i=0
while i<11:
    print('while number:',i)
    i= i+1
"""

#Iterate 10 to 0 using for loop, do the same using while loop.
"""
number.reverse()
for number in number:
    print('Reverse for number:', number)
i=10
while i>-1:
    print('Reverse while number:',i)
    i=i-1
"""

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#
##
###
####
#####
######
#######
"""
i=0
while i<8:
    print('#'*i)
    i=i+1
"""
#Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""
i=0
while i<9:
    print('# # # # # # # #')
    i=i+1
"""
#Print the following pattern
"""
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""
"""
i=0
while i <11:
    print(i,'X',i,'=',i*i)
    i=i+1
"""
#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
"""
dev_env=['Python', 'Numpy','Pandas','Django', 'Flask']
for dev_env in dev_env:
    print(dev_env)
"""
#Use for loop to iterate from 0 to 100 and print only even numbers
"""
for num in range(0,100):
    if num%2==0:
        print(num)
"""
#Use for loop to iterate from 0 to 100 and print only odd numbers
"""
for num in range(0,100):
    if num%2==1:
        print(num)
"""

#Exercises: Level 2

#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
"""
sum_num=0
for num in range(0,101):
    sum_num = num+sum_num
    print(sum_num)
"""

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
"""
sum_even=0
sum_odd=0
for num in range(0,101):
    if num%2==1:
        sum_odd = num+sum_odd
        print('sum odd numbers:', sum_odd)
    if num%2==0:
        sum_even = num+sum_even
        print('sum even numbers: ', sum_even)
"""

#Exercises: Level 3

#Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
"""
for country in countries:
    print(country)
"""

#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
"""
fruit=['banana', 'orange', 'mango', 'lemon']
cantidad_frutas= int(len(fruit))
i=-1
while i>=-cantidad_frutas:
    print(fruit[i])
    i= i-1
"""

#Go to the data folder and use the countries_data.py file.
    #What are the total number of languages in the data
"""
idiomas_unicos = set()
for pais in paises:
    idiomas = pais.get('languages', [])
    idiomas_unicos.update(idiomas)
print('hay un total de:',len(idiomas_unicos),'idiomas')
"""
    #Find the ten most spoken languages from the data
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

    #Find the 10 most populated countries in the world
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



