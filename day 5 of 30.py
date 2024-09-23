#Declare an empty list
"""
list=[]
"""

#Declare a list with more than 5 items
"""
colores=['azul','rojo','verde','amarillo','celeste']
"""

#Find the length of your list
"""
colores=['azul','rojo','verde','amarillo','celeste']
print(len(colores))
"""

#Get the first item, the middle item and the last item of the list
"""
colores=['azul','rojo','verde','amarillo','celeste']
print('Primer color: ', colores[1])
print('Color medio: ', colores[int((len(colores))/2)])
print('Ultimo color: ', colores[-1])
"""

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
"""
mixed_data_type= ['Jorge', 24, 1.8,'soltero','doxed']
"""

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
"""
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#Print the list using print()
print(it_companies)

#Print the number of companies in the list
print('cantidad de empresas TI: ', len(it_companies))

#Print the first, middle and last company
print('Primer compañia ', it_companies[1])
print('Compañia medio: ', it_companies[int((len(it_companies))/2)])
print('Ultima compañia: ', it_companies[-1])

#Print the list after modifying one of the companies
print(it_companies)
it_companies[3]= 'apol'
print(it_companies)

#Add an IT company to it_companies
print(it_companies)
it_companies.append('Nvidia')
print(it_companies)

#Insert an IT company in the middle of the companies list
print(it_companies)
it_companies.insert(int((len(it_companies))/2),'AMD')
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
mayus=it_companies[2].upper()
it_companies[2]=mayus
print(it_companies)


#Join the it_companies with a string '#;  '
union = '#;  '.join(it_companies)
print(union)

#Check if a certain company exists in the it_companies list.
check_oracle= 'Oracle' in it_companies
print('Existe "Oracle en las compañias de TI?: "', check_oracle)

#Sort the list using sort() method
it_companies.sort()
print(it_companies)

#Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

#Slice out the first 3 companies from the list
print(it_companies[3:])

#Slice out the last 3 companies from the list
print(it_companies[:-3])

#Slice out the middle IT company or companies from the list
print(it_companies[:(int((len(it_companies))/2))] + it_companies[(int((len(it_companies))/2))+1:] )

#Remove the first IT company from the list
it_companies.remove(it_companies[0])
print(it_companies)

#Remove the middle IT company or companies from the list
it_companies.remove(it_companies[(int((len(it_companies))//2))])
print(it_companies)

#Remove the last IT company from the list
it_companies.remove(it_companies[-1])
print(it_companies)

#Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#Destroy the IT companies list
del it_companies
print(it_companies)
"""

#Join the following lists:

#front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#back_end = ['Node','Express', 'MongoDB']
"""
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
fua_man= front_end+back_end
print(fua_man)

#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

full_stack=fua_man.copy()
print(full_stack)
"""
#Exercises: Level 2

#    The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#    Sort the list and find the min and max age
"""
ages.sort()
print('La edad minima es: ', ages[0])
print('La edad maxima es: ', ages[-1])


#    Add the min age and the max age again to the list

edad_minima= ages[0]
edad_maxima= ages[-1]
ages.append(edad_maxima)
ages.append(edad_minima)
print(ages)


#    Find the median age (one middle item or two middle items divided by two)

print('La edad media es: ', ages[(int(len(ages)))//2])


#    Find the average age (sum of all items divided by their number )

i=0
suma_promedio=0
while i<len(ages):
    suma_promedio= ages[i] + suma_promedio
    i+=1
print('El promedio de edades es: ', suma_promedio/len(ages))


#    Find the range of the ages (max minus min)

ages.sort()
rango_edad=ages[-1]-ages[0]
print('El rango de edades es: ', rango_edad)


#    Compare the value of (min - average) and (max - average), use abs() method

ages.sort()
min_avg=ages[0]-suma_promedio/len(ages)
max_avg=ages[-1]-suma_promedio/len(ages)
print('El absoluto de las medias es la misma: ',abs(min_avg) is abs(max_avg)) 
"""

#    Find the middle country(ies) in the countries list
"""
countries = ['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi','Cambodia','Cameroon','Canada','Cape Verde','Central African Republic','Chad','Chile','China','Colombi','Comoros','Congo (Brazzaville)','Congo','Costa Rica',"Cote d'Ivoire",'Croatia','Cuba','Cyprus','Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic','East Timor (Timor Timur)','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Ethiopia','Fiji','Finland','France','Gabon','Gambia, The','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Honduras', 'Hungary', 'Iceland', 'India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Korea, North','Korea, South','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco','Mongolia','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands','New Zealand','Nicaragua','Niger','Nigeria','Norway','Oman','Pakistan','Palau','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal','Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis','Saint Lucia','Saint Vincent','Samoa','San Marino','Sao Tome and Principe','Saudi Arabia','Senegal','Serbia and Montenegro','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','Spain','Sri Lanka','Sudan','Suriname','Swaziland','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Uzbekistan','Vanuatu','Vatican City','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe',]

cantidad_paises=len(countries)
pais_medio= cantidad_paises/2
if pais_medio % 2 == 0:
    medio_1=cantidad_paises//2
    print('El pais de enmedio es: ',countries[medio_1])
else:
    medio_1=cantidad_paises//2
    medio_2=medio_1+1
    print('los paises de enmedio son: ',countries[medio_1],' y ', countries[medio_2])


#    Divide the countries list into two equal lists if it is even if not one more country for the first half.
corte=medio_1+1
primera_mitad=countries[0:corte]
segunda_mitad=countries[corte:]
print('Son: ',len(primera_mitad),primera_mitad)
print('Son: ',len(segunda_mitad),segunda_mitad)
"""

#    ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
"""
paises=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
pais_1,pais_2,pais_3,*escandinavos=paises
print(pais_1)
print(pais_2)
print(pais_3)
print(escandinavos)
"""