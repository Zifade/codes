import math
#The radius of a circle is 30 meters.
#
#    Calculate the area of a circle and assign the value to a variable name of area_of_circle
#    Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
#    Take radius as user input and calculate the area.
#
#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

radio = 30
area_del_circulo = math.pi*radio**2
perimetro_del_circulo = 2*math.pi*radio

print('el area predefinida es: ', area_del_circulo)
print('el perimetro predefinido es: ', perimetro_del_circulo)

radio_usuario = input('Ingresa un radio personalizado: ')
radio_usuario_int = int(radio_usuario)
area_del_circulo_usuario = math.pi*radio_usuario_int**2
perimetro_del_circulo_usuario = 2*math.pi*radio_usuario_int

print('el area predefinida es:', area_del_circulo_usuario)
print('el perimetro predefinido es:', perimetro_del_circulo_usuario)
