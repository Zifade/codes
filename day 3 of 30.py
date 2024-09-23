from random import randrange
import math
#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
"""
altura_triangulo_input = input('introduzca la altura de un triangulo : ')
base_triangulo_input = input('introduzca la base de un triangulo : ')
area_triangulo = (float(altura_triangulo_input)*float(base_triangulo_input))/2

print('El area del triangulo es: ', area_triangulo)
"""

#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle
"""
triangulo_lado_a=input('introduzca la medida del lado A del triangulo: ')
triangulo_lado_b=input('introduzca la medida del lado B del triangulo: ')
triangulo_lado_c=input('introduzca la medida del lado C del triangulo: ')

perimetro_trianglo= float(triangulo_lado_a)+float(triangulo_lado_b)+float(triangulo_lado_c)
print('El perimetro del tiangulo es: ', perimetro_trianglo)
"""

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
"""
rectangulo_lado_a=input('Introduzca el largo del rectangulo: ')
rectangulo_lado_b=input('Introduzca el ancho del rectangulo: ')
rectangulo_area=float(rectangulo_lado_a)*float(rectangulo_lado_b)
print('El area del rectangulo es: ',rectangulo_area)
"""

#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
"""
radio_circumferencia= input('Introduzca el radio de la circumferencia: ')
pi=3.14
area__circumferencia=pi*(float(radio_circumferencia)**2)
perimetro_circumferencia=pi*float(radio_circumferencia)*2
print('El area de la circumferencia es: ',area__circumferencia)
print('El perimetro de la circumferencia es: ',perimetro_circumferencia)
"""

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
"""
def funcion(x):
    return 2*x-2

punto_a= randrange(1, 20)
punto_b= randrange(1, 20)
f_a= funcion(punto_a)
f_b= funcion(punto_b)
pendiente_8= (f_b-f_a)/(punto_b-punto_a)
print('La pendiente es: ',pendiente_8)
interseccion_x = 0
interseccion_x_y= funcion(interseccion_x)
print('La interseccion de x con y se da en el punto: ',interseccion_x_y)
interseccion_x_x= 2/2 #0=2x-2 -> 2=2x -> 2/2=x
print('La interseccion de y con x se da en el punto: ',interseccion_x_x)
"""

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
"""
x_1=2
x_2=6
y_1=2
y_2=10
pendiente_9= (y_2-y_1)/(x_2-x_1)
print('La pendiente es: ',pendiente_9)
distancia_euclidiana= math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
print('La distancia euclidiana es: ',distancia_euclidiana)
"""

#Compare the slopes in tasks 8 and 9.
"""
print(pendiente_8 > pendiente_9)
print(pendiente_8 >= pendiente_9)
print(pendiente_8 < pendiente_9)
print(pendiente_8 < pendiente_9)
print(pendiente_8 <= pendiente_9)
print(pendiente_8 == pendiente_9)
print(pendiente_8 != pendiente_9)
"""

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
"""
x=1
y=1
while y>0:
    y= x**2 +6*x+9
    x-=1
    print('valor de y es: ',y)
print('El valor de y es: ',y ,' El valor de x es: ',x)
"""

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
"""
largopy= len('python')
largodra= len('dragon')
print(largodra<largopy)
"""

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
"""
print('hay "on" en python? ', 'on' in 'python')
print('hay "on" en dragon? ', 'on' in 'dragon')
"""

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
"""
print('hay "jargon" en la oración? ', 'jargon' in 'I hope this course is not full of jargon')
"""
#There is no 'on' in both dragon and python
"""
print('no hay "on" en python? ', 'on' not in 'python')
print('no hay "on" en dragon? ', 'on' not in 'dragon')
"""
#Find the length of the text python and convert the value to float and convert it to string
"""
a=len('python')
print('python tiene ',a, ' letras')
print(float(a),' letras')
print(str(a),' letras')
"""

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
"""
numero_usuario = input('Ingresa un numero: ')
numero_usuario_int = int(numero_usuario)
if numero_usuario_int%2==0:
    print('El numero es par!')
else:
    print('El numero es impar!')
"""

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
"""
cociente_floor = 7//3
cociente =2.7
print('cociente floor ',cociente_floor,' cociente ',cociente,'.son el mismo numero? ', cociente is cociente_floor)
"""

#Check if type of '10' is equal to type of 10
"""
int_10 = 10
str_10 = '10'

print('"10" is a: ',type(str_10))
print('10 is a: ',type(int_10))
"""

#Check if int('9.8') is equal to 10
"""
print(9.8 == 10)
"""

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
"""
horas_trabajadas=input('Ingresa la cantidad de horas que trabajas: ')
Pago_hora=input('Ingresa cuanto vale cada hora que trabajas: ')
sueldo=int(horas_trabajadas)*int(Pago_hora)
print('Tu sueldo es de: ',sueldo)
"""

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
"""
edad_usuario=input('Ingresa tu edad: ')
vida_restante = 100-int(edad_usuario)
segundos_restantes=vida_restante*12*30*24*60*60
print('Te quedan ',segundos_restantes,' segundos de vida')
"""

#Write a Python script that displays the following table    
"""
print('1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125')
"""