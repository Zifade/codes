import statistics
from collections import Counter

#---Exercises LVL 1

#Python has the module called statistics and we can use this module to do all the statistical calculations.
#However, to learn how to make function and reuse function let us try to develop a program, which calculates:
# a)the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation).
# b)In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample.
# You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class.
# Check the output below.

"""
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range() # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
"""
# you output should look like this
"""
print(data.describe())
Count: 25
Sum:  744
Min:  24
Max:  38
Range:  14
Mean:  30
Median:  29
Mode:  (26, 5)
Variance:  17.5
Standard Deviation:  4.2
Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
"""

#----------
"""
class estadisticas:
    def __init__(self, ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]):
        self.data= ages
    
    #--Trabajo de datos

    def central_tendency(self):
    #mean, median, mode
        media_datos=statistics.mean(self.data)
        mediana_datos=statistics.median(self.data)
        moda_datos=statistics.mode(self.data)
        return f'La tendencia central es:\nLa media: {media_datos} \nLa mediana: {mediana_datos}\nLa moda: {moda_datos}'
    
    def measure_of_variability(self):
    #range, variance, standard deviation
        rango_datos=max(self.data) - min(self.data)
        varianza_datos=statistics.pvariance(self.data)
        desviacion_estandar=statistics.stdev(self.data)
        return f'Las medidas de variabilidad son: \nRango de datos: {rango_datos}\nVarianza de datos: {varianza_datos}\nDesviación estándar: {desviacion_estandar}'
    
    def mmcp(self):
    #min, max, count, percentile
        minimo_datos=min(self.data)
        maximo_datos=max(self.data)
        conteo_datos=len(self.data)
        percentil_datos=statistics.quantiles(self.data)
        return f'El dato menor es: {minimo_datos}\nEl dato mayor es: {maximo_datos}\nEl total de datos es: {conteo_datos}\nEl percentil de los datos es: {percentil_datos}'
    
    def frequency_distribution(self):
        frecuencias = Counter(self.data)
        frecuencias_ordenadas = sorted(frecuencias.items(), key=lambda x: (-x[1], x[0]))
        
        resultado = []
        for i, (numero, frecuencia) in enumerate(frecuencias_ordenadas):
            if i == 0:
                resultado.append(f"El dato más repetido es: {numero} con un total de {frecuencia} veces")
            else:
                resultado.append(f"El siguiente dato es: {numero} con un total de {frecuencia} veces")
        
        return "\n".join(resultado)
    
edades=estadisticas()

print(edades.data)
print(edades.central_tendency())
print(edades.measure_of_variability())
print(edades.mmcp())
print(edades.frequency_distribution())
"""

#---Exercises LVL 2

#Create a class called PersonAccount.
# It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense
# and account_balance methods.
# Incomes is a set of incomes and its description. The same goes for expenses.

