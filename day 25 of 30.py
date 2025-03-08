import pandas as pd
import numpy  as np


#Read the hacker_news.csv file from data directory
with open(r'data\hacker_news.csv') as text:
    hack_df=pd.read_csv(text)
"print(hack_df)"

#Get the first five rows

"print('Las primeras 5 filas: \n', hack_df.head())"


#Get the last five rows
"print('Las ultimas 5 filas: \n',hack_df.tail())"

#Get the title column as pandas series
"print('las columnas son: \n', hack_df.columns)"

#Count the number of rows and columns
"print('Numero de columnas y filas: ', hack_df.shape)"

#--

    #Filter the titles which contain python

python_rows = hack_df[hack_df['title'].str.contains('python', case=False)]

for index, row in python_rows.iterrows():
    print(f"ID: {row['id']}, Título: {row['title']}")

    #Filter the titles which contain JavaScript

js_rows = hack_df[hack_df['title'].str.contains('javascript', case=False)]

for index, row in js_rows.iterrows():
    print(f"ID: {row['id']}, Título: {row['title']}")

    #Explore the data and make sense of it
if len(python_rows)> len(js_rows):
    print('Python es más comun en las noticias de hacking \n Python news: ', len(python_rows), 'JavaScript news:', len(js_rows))
if len(python_rows)< len(js_rows):
    print('JavaScript es más comun en las noticias de hacking \n Python news: ', len(python_rows), 'JavaScript news:', len(js_rows))
if len(python_rows) == len(js_rows):
    print('Python y JavaSript son igual de comunes en las noticias de hacking \n Python news: ', len(python_rows), 'JavaScript news:', len(js_rows))



