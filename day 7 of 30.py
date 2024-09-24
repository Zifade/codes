#sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


#Exercises: Level 1
"""
#    Find the length of the set it_companies
print('El largo de it_companies es: ', len(it_companies))

#    Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#    Insert multiple IT companies at once to the set it_companies
otras_IT=('OpenIA', 'Nvidia', 'AMD')
it_companies.update(otras_IT)
print(it_companies)

#    Remove one of the companies from the set it_companies
objeto_eliminado=it_companies.pop()
print('Se eliminó: "',objeto_eliminado, '" de IT_Companies')
print(it_companies)
#    What is the difference between remove and discard
#    Discard no levanta errores de metodo cuando se le indica un objeto que no exista en el set
"""
#Exercises: Level 2
"""
#    Join A and B
AUB= A.union(B)
print('Set A: ', A)
print('Set B: ', B)
print('Union de A y B: ',AUB)

#    Find A intersection B
AIB= A.intersection(B)
print('Intersección de A y B: ',AIB)

#    Is A subset of B
print('Es A un subset de B? ', A.issubset(B))

#    Are A and B disjoint sets
print('Es A un disjoint de B? ', A.isdisjoint(B))

#    Join A with B and B with A
AUB= A.union(B)
BUA= B.union(A)
print('Union de A y B: ',AUB)
print('Union de B y A: ',BUA)
#   What is the symmetric difference between A and B
symetric_diff= A.symmetric_difference(B)
print('Diferencia simetrica entre A y B: ',symetric_diff)

#    Delete the sets completely
del A
del B
print('Set A: ',A,' Set B: ',B)
"""
#Exercises: Level 3
"""
#    Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age
set_age=set(age)
print(set_age)
lst_len=int(len(age))
set_len=int(len(set_age))
if lst_len>set_len:
    print('La lista(',lst_len ,') es más larga que el set(', set_len,')')
else:
    print('El set(',set_len ,') es más largo que la lista(', lst_len,')')

#    Explain the difference between the following data types: string, list, tuple and set
#Los strings son valores de texto, no se pueden calcular
#Las listas son un conjunto de objetos de una misma o distinta naturaleza y la lista es modificable
#Tuple es como las listas pero son inmutables, no se pueden modificar
#El set es una lista de items unicos, es decir, que no se pueden repetir dentro de la misma. Y a los que se les puede aplicar analisis de conjuntos matematicos
"""
#    I am a teacher and I love to inspire and teach people.
# How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
"""
frase=('I am a teacher and I love to inspire and teach people')
frase_separada= frase.split()
print(frase_separada,'se compone de: ',len(frase_separada),' palabras')
set_frase=set(frase_separada)
print('hay un total de: ',len(set_frase),' de palabras unicas')
"""
