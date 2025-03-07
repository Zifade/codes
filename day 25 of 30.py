import pandas as pd
import numpy  as np

#Read the hacker_news.csv file from data directory
#Get the first five rows
"print(df.head())"
#Get the last five rows
"print(df.tail())"
#Get the title column as pandas series
#Count the number of rows and columns
    #Filter the titles which contain python
    #Filter the titles which contain JavaScript
    #Explore the data and make sense of it


data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'},
    {'Name': 'Zidane', 'Country': 'Kingdom', 'City': 'Alexandria'}]
df = pd.DataFrame(data)
print(df)
print(df.shape)

