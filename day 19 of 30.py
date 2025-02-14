import re
from collections import Counter
import json
from stop_words import stop_words
from typing import Set
import csv
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
print(find_most_common_words(words_string,10))
#   b) The ten most frequent words used in Michelle's speech
with open(r'data\michelle_obama_speech.txt') as text:
    words_string=text.read()
print(find_most_common_words(words_string,10))
#   c) The ten most frequent words used in Trump's speech
with open(r'data\donald_speech.txt') as text:
    words_string=text.read()
print(find_most_common_words(words_string,10))
#   d) The ten most frequent words used in Melina's speech
with open(r'data\melina_trump_speech.txt') as text:
    words_string=text.read()
print(find_most_common_words(words_string,10))
"""

#Write a python application that checks similarity between two texts.
#   It takes a file or a string as a parameter and it will evaluate the similarity of the two texts.
#   For instance check the similarity between the transcripts of Michelle's and Melina's speech.
#   You may need a couple of functions, function to clean the text(clean_text),
#   function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity).
#   List of stop words are in the data directory
"""
def clean_text(text_to_clean: str) -> str:
    cleaned_text = re.sub('[,.-:;"]', '', text_to_clean)
    return cleaned_text.lower()

def remove_support_words(full_text: str, stop_words: list) -> str:
    words = full_text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def check_similarity(text_1: str, text_2: str, stop_words: list) -> dict:
    clean_text_1 = clean_text(text_1)
    clean_text_2 = clean_text(text_2)
    basic_text_1 = remove_support_words(clean_text_1, stop_words)
    basic_text_2 = remove_support_words(clean_text_2, stop_words)
    
    words_1: Set[str] = set(basic_text_1.split())
    words_2: Set[str] = set(basic_text_2.split())
    
    shared_words = words_1.intersection(words_2)
    
    similarity_metrics = {
        "shared_words": list(shared_words),
        "number_of_shared_words": len(shared_words),
        "percentage_text_1": round(len(shared_words) / len(words_1) * 100, 2),
        "percentage_text_2": round(len(shared_words) / len(words_2) * 100, 2)
    }
    
    return similarity_metrics

if __name__ == "__main__":
    with open(r'data/michelle_obama_speech.txt') as mt:
        michelle_speech = mt.read()
    
    with open(r'data/melina_trump_speech.txt') as text:
        melania_speech = text.read()
    
    result = check_similarity(michelle_speech, melania_speech, stop_words)

    print("Análisis de similitud entre los discursos:")
    print(f"Número de palabras compartidas: {result['number_of_shared_words']}")
    print(f"Porcentaje del discurso de Michelle: {result['percentage_text_1']}%")
    print(f"Porcentaje del discurso de Melania: {result['percentage_text_2']}%")
    print("\nPalabras compartidas:")
    print(", ".join(result['shared_words']))
"""

#Find the 10 most repeated words in the romeo_and_juliet.txt
"""
def find_most_common_words(text_in,amount):
    qty=int(amount)
    text_in = text_in.lower()
    words = re.findall(r'\b\w+\b', text_in)
    word_counts = Counter(words)
    most_common = word_counts.most_common(int(amount))
    return most_common

with open(r'data\romeo_and_juliet.txt') as text:
    words_string=text.read()

print(find_most_common_words(words_string,10))
"""

#Read the hacker news csv file and find out:
"""
#   a) Count the number of lines containing python or Python

with open('data\hacker_news.csv') as hack_news:
    csv_reader = csv.reader(hack_news, delimiter=',')
    line_count = 0
    lines_with_python = 0
    for row in csv_reader:
        if 'python' in row[1].lower():
            lines_with_python += 1
    print(f'Number of lines with Python: {lines_with_python}')


#   b) Count the number lines containing JavaScript, javascript or Javascript

with open('data\hacker_news.csv') as hack_news:
    csv_reader = csv.reader(hack_news, delimiter=',')
    next(csv_reader)
    lines_with_js = 0
    for row in csv_reader:
        if 'javascript' in row[1].lower():
            lines_with_js +=1
    print(f'Number of lines with JavaScript:  {lines_with_js}')

#   c) Count the number lines containing Java and not JavaScript
with open('data\hacker_news.csv') as hack_news:
    csv_reader = csv.reader(hack_news, delimiter=',')
    next(csv_reader)
    lines_with_jv = 0
    for row in csv_reader:
        if 'java' in row[1].lower():
            lines_with_jv +=1
        if 'javascript' in row[1].lower():
            lines_with_jv +=-1
    print(f'Number of lines with only Java:  {lines_with_jv}')
"""