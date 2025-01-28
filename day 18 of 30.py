import re
from collections import Counter
#---Exercises LVL 1

#What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

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


#The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 
# 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
"""
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12) # 20
"""


#---Exercises LVL 2

#Write a pattern which identifies if a string is a valid python variable
"""
is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True
"""

#---Exercises LVL 3

#Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
