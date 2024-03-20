import os
import time
import pandas

# Exmplanation for this fix
# https://stackoverflow.com/questions/4060221/how-to-reliably-open-a-file-in-the-same-directory-as-the-currently-running-scrip

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Imported pandas, to read a CSV file, 
# Imported os and time, to utilize sleep function
while True:
    if os.path.exists(os.path.join(__location__ , "temps_today.csv")):
        # pandas when reading returns DataFrame object type
        data = pandas.read_csv(os.path.join(__location__, 'temps_today.csv'))
        
        # mean of only st1 column
        print(data.mean()['st1'])
    else:
        print('File does not exist !')
    time.sleep(5)

