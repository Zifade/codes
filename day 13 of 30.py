#Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

"""
positive_number=[i for i in numbers if i>0]
print(positive_number)
"""
#Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

"""
flat_list=[number for row in list_of_lists for sublist in row for number in sublist]
print(flat_list)
"""

#Using list comprehension create the following list of tuples:
"""
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
"""
"""
power_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

for tuple in power_tuples:
    print(tuple)
"""

#Flatten the following list to a new list:
"""
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
"""
"""
flat_country=[[country.capitalize(), country[:3].capitalize(), city.capitalize()] for [country, city] in [item[0] for item in countries]]
print(flat_country)
"""

#Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
"""
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
"""
"""
result = [{'country': country.upper(), 'city': city.upper()} for [(country, city)] in countries]
print(result)
"""
#Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
"""
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
"""
"""
flat_list=[f"{first_name} {last_name}" for [(first_name, last_name)] in names]
print(flat_list)
"""
#Write a lambda function which can solve a slope or y-intercept of linear functions.
"""
slope=lambda x1,y1,x2,y2: (y2 - y1) / (x2 - x1)
print(slope(3,5,7,4))
"""