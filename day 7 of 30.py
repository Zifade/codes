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

#Exercises: Level 3

#    Convert the ages to a set and compare the length of the list and the set, which one is bigger?
#    Explain the difference between the following data types: string, list, tuple and set
#    I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
