import re
from collections import Counter
import json
#---Exercises LVL1


#Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
# a) Read obama_speech.txt file and count number of lines and words
"""
with open(r'data\obama_speech.txt') as text:
    lines = text.readlines()
print('Cantidad de lineas(B_Obama): ',len(lines))
with open(r'data\obama_speech.txt') as text:
    s_txt= text.read()
palabras= s_txt.split()
print('Cantidad de palabras(B_Obama)', len(palabras))
"""

# b) Read michelle_obama_speech.txt file and count number of lines and words
"""
with open(r'data\michelle_obama_speech.txt') as text:
    lines = text.readlines()
print('Cantidad de lineas(M_Obama): ',len(lines))
with open(r'data\michelle_obama_speech.txt') as text:
    s_txt= text.read()
palabras= s_txt.split()
print('Cantidad de palabras(M_Obama)', len(palabras))
"""

# c) Read donald_speech.txt file and count number of lines and words
"""
with open(r'data\donald_speech.txt') as text:
    lines = text.readlines()
print('Cantidad de lineas(D_Trump): ',len(lines))
with open(r'data\donald_speech.txt') as text:
    s_txt= text.read()
palabras= s_txt.split()
print('Cantidad de palabras(D_Trump)', len(palabras))
"""

# d) Read melina_trump_speech.txt file and count number of lines and words
"""
with open(r'data\melina_trump_speech.txt') as text:
    lines = text.readlines()
print('Cantidad de lineas(M_Trump): ',len(lines))
with open(r'data\melina_trump_speech.txt') as text:
    s_txt= text.read()
palabras= s_txt.split()
print('Cantidad de palabras(M_Trump)', len(palabras))
"""

#Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
"""
with open(r'data/countries_data.json', encoding='utf-8') as countries_json:
    countries_dct = json.load(countries_json)

n=10
contador_idiomas = Counter()
for country in countries_dct:
    population = country.get('population', 0)
    languages = country.get('languages', [])
    if languages:
        speakers_per_language = population / len(languages)
        for language in languages:
            contador_idiomas[language] += speakers_per_language

top_10_languages = contador_idiomas.most_common(10)
print("\nLos 10 idiomas más hablados:")
print("-" * 50)
for i, (language, speakers) in enumerate(top_10_languages, 1):
    speakers_millions = speakers / 1_000_000
    print(f"{i}. {language:<15} {speakers_millions:,.1f} millones de hablantes")
"""
#Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
"""
with open(r'data/countries_data.json', encoding='utf-8') as countries_json:
    countries_dct = json.load(countries_json)

countries_by_population = sorted(countries_dct, key=lambda x: x['population'], reverse=True)
top_10_countries = countries_by_population[:10]

print("\nLos 10 países más poblados:")
print("-" * 50)
for i, country in enumerate(top_10_countries, 1):
    population_millions = country['population'] / 1_000_000
    print(f"{i}. {country['name']:<15} {population_millions:,.1f} millones de habitantes")
"""
#---Exercises LVL2


#Extract all incoming email addresses as a list from the email_exchange_big.txt file.
"""
#   extractor de data
with open(r'data\email_exchanges_big.txt') as mail_reg:
    mail_data= mail_reg.read()

#   identificador de email
def is_mail(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, text)
    return set(emails)

lista_correos = is_mail(mail_data)
print("Correos encontrados:")
for email in lista_correos:
    print(email)
"""

#Find the most common words in the English language.
#   Call the name of your function find_most_common_words, it will take two parameters
#   - a string or a file and a positive integer, indicating the number of words.
#   Your function will return an array of tuples in descending order. Check the output
"""
def find_most_common_words(text_in,amount):
    qty=int(amount)
    text_in = text_in.lower()
    words = re.findall(r'\b\w+\b', text_in)
    word_counts = Counter(words)
    most_common = word_counts.most_common(int(amount))
    return most_common

with open(r'data\donald_speech.txt') as text:
    words_string=text.read()

print(find_most_common_words(words_string,5))
"""

#Use the function, find_most_frequent_words to find:
"""
#   a) The ten most frequent words used in Obama's speech
with open(r'data\obama_speech.txt') as text:
    words_string=text.read()
#   b) The ten most frequent words used in Michelle's speech
with open(r'data\michelle_obama_speech.txt') as text:
    words_string=text.read()
#   c) The ten most frequent words used in Trump's speech
with open(r'data\donald_speech.txt') as text:
    words_string=text.read()
#   d) The ten most frequent words used in Melina's speech
with open(r'data\melina_trump_speech.txt') as text:
    words_string=text.read()
"""

#Write a python application that checks similarity between two texts.
#   It takes a file or a string as a parameter and it will evaluate the similarity of the two texts.
#   For instance check the similarity between the transcripts of Michelle's and Melina's speech.
#   You may need a couple of functions, function to clean the text(clean_text),
#   function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity).
#   List of stop words are in the data directory

#Find the 10 most repeated words in the romeo_and_juliet.txt

#Read the hacker news csv file and find out:
#   a) Count the number of lines containing python or Python
#   b) Count the number lines containing JavaScript, javascript or Javascript
#   c) Count the number lines containing Java and not JavaScript