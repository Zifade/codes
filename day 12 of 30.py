#Exercises: Level 1
from random import *
import string
#Write a function which generates a six digit/character random_user_id. 
"""
def random_user_id(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

print(random_user_id())
"""

#Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input().
#One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
"""
def random_user_id(size=int(input('Ingresa la cantidad de digitos: ')), qty=int(input('Ingresa la cantidad de ids: ')),chars=string.ascii_uppercase + string.digits):
    ids=[]
    for a in range(0,qty):
        ids.append(''.join(random.choice(chars) for _ in range(size)))
    return ids

print(random_user_id())
"""

#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
"""
def rgb_color_gen():
    rgb=[]
    for num in range(0,3):
      rgb.append(randrange(0,255))
    return rgb
print(rgb_color_gen())
"""

#Exercises: Level 2

#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols,
# 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
"""
def list_of_hexa_color(count):
    hex_array=[]
    i=0
    while i<count:
        color = randrange(0, 2**24)
        hex_color= hex(color)
        std_hex="#"+hex_color[2:]
        hex_array.append(std_hex)
        i+=1
    return hex_array
print(list_of_hexa_color(2))
"""

#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
"""
def rgb_color_gen(count):
    array_of_rgb=[]
    i=0
    while i<count:
        rgb=[]
        for num in range(0,3):
            rgb.append(randrange(0,255))
        array_of_rgb.append(rgb)
        i+=1
    return array_of_rgb
print(rgb_color_gen(5))
"""

#Write a function generate_colors which can generate any number of hexa or rgb colors.
"""
def generate_colors(tipo,count):
    tipo_color=tipo.lower()
    if tipo_color=="rgb":
        array_of_rgb=[]
        i=0
        while i<count:
            rgb=[]
            for num in range(0,3):
                rgb.append(randrange(0,255))
            array_of_rgb.append(rgb)
            i+=1
        return array_of_rgb
    if tipo=="hexa":
        hex_array=[]
        i=0
        while i<count:
            color = randrange(0, 2**24)
            hex_color= hex(color)
            std_hex="#"+hex_color[2:]
            hex_array.append(std_hex)
            i+=1
        return hex_array
print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))
"""

#Exercises: Level 3

#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
"""
def shuffle_list(list=[]):
    shuffle(list)
    return list
print(shuffle_list([1,4,6,8,5,5,7,4,3,4,6]))
"""

#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
"""
def seven_number_gen():
    numbers = list(range(10))
    shuffle(numbers)
    return numbers[:7]
print(seven_number_gen())
"""