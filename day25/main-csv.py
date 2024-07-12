'''with open("weather_data.csv") as data_file:
    data = data_file.readlines() #her satiri listeye atar. '''

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file) #created csv reader object
    temperatures = []
    for row in data:
        #print(row)
        if row[1] == "temp":
            continue
        temperatures.append(int(row[1]))
    
    print(temperatures)    
