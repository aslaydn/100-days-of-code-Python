import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average_temp = round(sum(temp_list) / len(temp_list),2)
print(average_temp) 
print(data["temp"].mean())

print(data["temp"].max())

#get data in columns
print(data["condition"])
print(data.condition)

#get data in rows
print(data[data.day == "Monday"])
#print max temp row
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

#Create a dataframe from scratch
grades_dict = {
    "student": ["Amy","James","Angela"],
    "scores": [76,56,65]
}

grades = pandas.DataFrame(grades_dict)
grades.to_csv("new_data.csv")