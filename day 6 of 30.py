
#    Create an empty tuple
"""
tuple_1= tuple()
"""

#    Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
"""
hermanos=('Martin','nicolas','jose','benjamin')
print(hermanos)
"""

#    Join brothers and sisters tuples and assign it to siblings
"""
hermanos=('martin','jose','nicolas')
hermanas=('valentina','javiera','barbara')
siblings= hermanos+hermanas
print(siblings)


#    How many siblings do you have?
print('tengo ',len(siblings),' hermanos')

#    Modify the siblings tuple and add the name of your father and mother and assign it to family_members
print('siblings: ',len(siblings))
mama=('marta','a')
print('mama ',mama)
familia= siblings+mama
print('familia ', familia)
"""
#    Unpack siblings and parents from family_members


#    Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
"""
frutas=('frutilla','manzana')
vegetales=('lechuga','papa')
animal=('cerdo','pavo')
print(frutas)
print(vegetales)
print(animal)
food_stuff_tp=frutas+vegetales+animal
print(food_stuff_tp)
"""


#    Change the about food_stuff_tp tuple to a food_stuff_lt list
"""
food_stuff_lst=list(food_stuff_tp)
print(food_stuff_lst)

"""

#    Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
"""
cantidad_comida=len(food_stuff_lst)
comida_medio= cantidad_comida/2
if comida_medio % 2 == 0:
    medio_1=cantidad_comida//2
    print('comida: ',food_stuff_lst[:medio_1], food_stuff_lst[medio_1:])
else:
    medio_1=cantidad_comida//2
    medio_2=medio_1+1
    print('comida: ',food_stuff_lst[:medio_1], food_stuff_lst[medio_2:])
"""

#    Slice out the first three items and the last three items from food_staff_lt list
"""
print(food_stuff_lst[2:-2])
"""

#    Delete the food_staff_tp tuple completely
"""
del food_stuff_tp
"""

#    Check if an item exists in tuple:
"""
print('pavo' in food_stuff_tp)
"""
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
"""
#    Check if 'Estonia' is a nordic country
print('es estonia un pais nordico?: ', 'Estonia' in nordic_countries)
#    Check if 'Iceland' is a nordic country
print('es islandia un pais nordico?: ','Iceland' in nordic_countries)
"""