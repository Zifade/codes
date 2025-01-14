#---Exercises LVL 1
from datetime import datetime

#Get the current day, month, year, hour, minute and timestamp from datetime module
"""
ahora= datetime.now()
dia= ahora.day
mes= ahora.month
anho= ahora.year
hora= ahora.hour
minuto= ahora.minute
timestamp= ahora.timestamp()
print(f'{dia}/{mes}/{anho}, {hora}:{minuto}')
print('timestamp', timestamp)
"""

#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
"""
ahora= datetime.now()
t= ahora.strftime("%m/%d/%Y, %H:%M:%S")
print('tiempo: ',t)
"""

#Today is 5 December, 2019. Change this time string to time.
"""
dia_concreto=datetime(2019,11,5)
print(dia_concreto)
"""

#Calculate the time difference between now and new year.
"""
ahora= datetime(year=2025, month=1, day=13)
new_year=datetime(year=2026, month=1, day=1)
resta_tiempo= ahora-new_year
print(resta_tiempo)
"""

#Calculate the time difference between 1 January 1970 and now.
"""
ahora= datetime(year=2025, month=1, day=13)
dia_concreto=datetime(year=1970, month=1, day=1)
resta_tiempo= ahora - dia_concreto
print(resta_tiempo)
"""

#Think, what can you use the datetime module for? Examples:
#    Time series analysis
#    To get a timestamp of any activities in an application
#    Adding posts on a blog
"""
-Para analizar fechas de publicacion
-Para poner limite temporal a funciones con "if"
-automatizar seasonal events
"""