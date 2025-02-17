import requests
import re
from collections import Counter
import numpy as np
import pandas as pd
#Read this url and find the 10 most frequent words. 'https://www.w3.org/TR/png/iso_8859-1.txt'
"""
url= 'https://www.w3.org/TR/png/iso_8859-1.txt'
response= requests.get(url)
text= response.text


def find_most_common_words(text_in,amount):
    text_in = text_in.lower()
    words = re.findall(r'\b\w+\b', text_in)
    word_counts = Counter(words)
    most_common = word_counts.most_common(int(amount))
    return most_common

print(find_most_common_words(text,10))
"""

#Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
cats_api = 'https://api.thecatapi.com/v1/breeds'
response= requests.get('https://api.thecatapi.com/v1/breeds')
cat_data= response.json()
#    a) the min, max, mean, median, standard deviation of cats' weight in metric units.
"""
def extract_weight_numbers(weight_str):
    numbers = [float(num.strip()) for num in weight_str.split('-')]
    return numbers

weights=[]

for cat in cat_data:
    metric_weight = cat['weight']['metric']
    min_weight, max_weight = extract_weight_numbers(metric_weight)
    weights.extend([min_weight, max_weight])

weights_array = np.array(weights)

min_weight = np.min(weights_array)
max_weight = np.max(weights_array)
mean_weight = np.mean(weights_array)
median_weight = np.median(weights_array)
std_weight = np.std(weights_array)
print(f'El peso minimo es: {min_weight:.2f} kg. El maximo es: {max_weight} kg')
print(f'El peso medio es: {mean_weight:.2f} kg. El mediano es: {median_weight:.2f} kg')
print(f'La desviacion estandar es: {std_weight:.2f} kg')
"""

#    b) the min, max, mean, median, standard deviation of cats' lifespan in years.
"""
def extract_weight_numbers(weight_str):
    numbers = [float(num.strip()) for num in weight_str.split('-')]
    return numbers

weights=[]

for cat in cat_data:
    metric_weight = cat['life_span']
    min_weight, max_weight = extract_weight_numbers(metric_weight)
    weights.extend([min_weight, max_weight])

weights_array = np.array(weights)

min_weight = np.min(weights_array)
max_weight = np.max(weights_array)
mean_weight = np.mean(weights_array)
median_weight = np.median(weights_array)
std_weight = np.std(weights_array)
print(f'La vida minima es de: {min_weight:.2f} años. La vida maxima es de : {max_weight} años')
print(f'La vida media es de: {mean_weight:.2f} años. la vida mediana es de : {median_weight:.2f} años')
print(f'La desviacion estandar es: {std_weight:.2f} años')
"""
#    c) Create a frequency table of country and breed of cats
"""
country_breeds = {}

for cat in cat_data:
    country = cat['country_code']
    breed = cat['name']
    if country not in country_breeds:
        country_breeds[country] = []

    country_breeds[country].append(breed)

print("Frecuencia de razas de gatos por país:")
for country, breeds in sorted(country_breeds.items()):
    print(f"\n{country}:")
    print(f"Número total de razas: {len(breeds)}")
    print("Razas:", ", ".join(breeds))
"""

#Read the countries API(404 page not found) and find

#    a) the 10 largest countries
#    b) the 10 most spoken languages
#    c) the total number of languages in the countries API
