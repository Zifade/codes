import re
from collections import Counter
#---Exercises LVL 1

#What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

"""
def count_words_regex(para):
    para = para.lower()
    words = re.findall(r'\b\w+\b', para)
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    most_common = max(word_counts.items(), key=lambda x: x[1])
    return most_common

palabra_comun = count_words_regex(paragraph)
print(f"Palabra más común: '{palabra_comun[0]}' (aparece {palabra_comun[1]} veces)")
"""



text='The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'
"""
positions= re.findall(r'-?\d+\.?\d*', text)
print(positions)
positions_int=list(map(int, positions))
print(positions_int)
distance_delta=positions_int[0]- positions_int[-1]
if distance_delta<0:
    distance_delta= distance_delta*-1
else:
    distance_delta
print(distance_delta)
"""

#---Exercises LVL 2

#Write a pattern which identifies if a string is a valid python variable
"""
def is_valid_variable(variable):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, variable))

is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
print(is_valid_variable('1first_name')) # False
is_valid_variable('firstname') # True
"""

#---Exercises LVL 3

#Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
