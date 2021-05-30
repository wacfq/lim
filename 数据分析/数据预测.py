import json
import csv

f = open("C:/Users/雪岩/Desktop/data.json", encoding='utf-8')
data = json.load(f)

y = []
for i in data:
    time = i['onlinetime']
    number = i['onlinenumber']
    change = i['onlinechange']

    x = [time, number, change]
    y.append(x)

print(y)

with open("C:/Users/雪岩/Desktop/预测.csv", "w", encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(y)

