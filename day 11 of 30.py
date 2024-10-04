#Exercises: Level 1

#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
"""
def suma(num1, num2):
    total= num1+ num2
    return total
print(suma(int(input('Escribe numero 1 de la suma: ')),int(input('Escribe numero 2 de la suma: '))))
"""

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
"""
def area_circulo(radio):
    PI= 3.14
    area= PI*radio*radio
    return area
print(area_circulo(int(input('Ingresa radio del cirulo: '))))
"""

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
"""
def add_all_nums(*nums):
    suma_num=0
    for i in nums:
        try:
            validate= int(i)
        except ValueError:
            print('Agregaste caracteres que no son numeros.')
            break
        suma_num+=i
    return suma_num
print(add_all_nums(4,6,8,4,2))
"""

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
"""
def celsius_to_farenheit(c):
    farenheit= (c*9/5)+32
    return farenheit
print('Los farenheit son: ',celsius_to_farenheit(int(input('Ingresa los grados Celsius: '))))
"""

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
"""
def check_season(mes_usuario):
    otoño=('septiembre','octubre','noviembre')
    invierno=('diciembre','enero','febrero')
    primavera=('marzo','abril','mayo')
    verano=('junio','julio','agosto')
    mes_user_low=mes_usuario.lower()
    if mes_user_low in otoño:
        print('Estas en la estacion de otoño')
    elif mes_user_low in invierno:
        print('Estas en la estacion de invierno')
    elif mes_user_low in primavera:
        print('Estas en la estacion de primavera')
    elif mes_user_low in verano:
        print('Estas en la estacion de verano')
    else:
        print('Ingresaste mal el mes')
    return ''
print(check_season(input('En que mes del año estas? ')))
"""

#Write a function called calculate_slope which return the slope of a linear equation
"""
def calculate_slope(y1,y2):
    slope= y2-y1
    return slope
print(calculate_slope(int(input('Ingresa Y1: ')),int(input('Ingresa Y2: '))))
"""

#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
"""
import math

def solve_quadratic_eqn(a, b, c):
    if a == 0:
        if b == 0:
            return "No es una ecuación cuadrática y no tiene solución única."
        else:
            return f"La ecuación es lineal con solución: {-c/b}"
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"Dos soluciones reales: x1 = {x1}, x2 = {x2}"
    elif discriminante == 0:
        x = -b / (2*a)
        return f"Una solución real (raíz doble): x = {x}"
    else:
        real = -b / (2*a)
        imag = math.sqrt(-discriminante) / (2*a)
        return f"Dos soluciones complejas: x1 = {real} + {imag}i, x2 = {real} - {imag}i"
print(solve_quadratic_eqn(1, 5, 6))
"""

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
"""
def print_list(list=[]):
    for list in list:
        print(list)
print(print_list([1,5,3,2,5]))
"""
#---------------------------------------------------------------------------------------------------------------------------
#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
"""
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
"""
#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
"""
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
"""
#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
"""
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]
"""
#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
"""
print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050
"""
#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

#Exercises: Level 2

#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
"""
print(evens_and_odds(100))
# The number of odds are 50.
# The number of evens are 51.
"""
#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
#Call your function is_empty, it takes a parameter and it checks if it is empty or not
#Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

#Exercises: Level 3

#Write a function called is_prime, which checks if a number is prime.
#Write a functions which checks if all items are unique in the list.
#Write a function which checks if all the items of the list are of the same data type.
#Write a function which check if provided variable is a valid python variable
#Go to the data folder and access the countries-data.py file.

#Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
#Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
