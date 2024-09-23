#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
"""
a='Thirty'
b='Days'
c='Of'
d='Python'
space=' '
challenge = a+space+b+space+c+space+d
print(challenge) 
"""

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
"""
space=' '
a='Coding'
b='For'
c='All'
cfa=a+space+b+space+c
print(cfa)
"""

#Declare a variable named company and assign it to an initial value "Coding For All".
"""
company= 'Coding for all'

#Print the variable company using print().
print(company)

#Print the length of the company string using len() method and print().
print(len(company))

#Change all the characters to uppercase letters using upper() method.
print(company.upper())

#Change all the characters to lowercase letters using lower() method.
print(company.lower())
#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string.
print(company[7:14])

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
index_check='Coding'
print(company.index(index_check))

#Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding','Python'))

#Change Python for Everyone to Python for All using the replace method or other methods.
pfe='Python for everyone'
print(pfe.replace('everyone','all'))

#Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())
"""

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
"""
big_tech='Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(big_tech.split(', '))
"""
#What is the character at index 0 in the string Coding For All.
"""
cfa='Coding For All'
print(cfa[0])
"""

#What is the last index of the string Coding For All.
"""
cfa='Coding For All'
print(cfa[-1])
"""

#What character is at index 10 in "Coding For All" string.
"""
cfa='Coding For All'
print(cfa[10])
"""

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
"""
cfa='Python For Everyone'
cfa_list=cfa.split()
print(cfa_list[0][0],cfa_list[1][0],cfa_list[2][0])
"""

#Create an acronym or an abbreviation for the name 'Coding For All'.
"""
cfa='Coding For All'
cfa_list=cfa.split()
print(cfa_list[0][0],cfa_list[1][0],cfa_list[2][0])
"""

#Use index to determine the position of the first occurrence of C in Coding For All.
"""
cfa='Coding For All'
print(cfa.index('C'))
"""

#Use index to determine the position of the first occurrence of F in Coding For All.
"""
cfa='Coding For All'
print(cfa.index('F'))
"""

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
"""
cfa='Coding For All'
print(cfa.rfind('l'))
"""

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
"""
sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
"""

#Use rindex to find the position of the last occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
"""
sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))
"""

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
"""
sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.replace('because because because', ''))
"""

#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
"""
sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
"""

#Does 'Coding For All' start with a substring Coding?
"""
cfa='Coding For All'
print(cfa.startswith('Coding'))
"""

#Does 'Coding For All' end with a substring coding?
"""
cfa='Coding For All'
print(cfa.endswith('Coding'))
"""

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
"""
cfa='   Coding For All      '
print(cfa.strip(' '))
"""

#Which one of the following variables return True when we use the method isidentifier():
#    30DaysOfPython
#    thirty_days_of_python
"""
intd='30DaysOfPython'
strd='thirty_days_of_python'
print('"30DaysOfPython" isidentifier? ',intd.isidentifier())
print('"thirty_days_of_python" isidentifier? ',strd.isidentifier())
"""

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
"""
libraries= ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
union= ' '.join(libraries)
print(union)
"""

#Use the new line escape sequence to separate the following sentences.
#'I am enjoying this challenge.'
#'I just wonder what is next.'
"""
print('I am enjoying this challenge.\nI just wonder what is next.')
"""

#Use a tab escape sequence to write the following lines.
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki
"""
print('Name\tAge\tCountry\tCity\t\nAsabeneh\t250\tFinland\tHelsinki\t')
"""

#The area of a circle with radius 10 is 314 meters square.
"""
area=3.14*(10**2)
print(area)
"""
