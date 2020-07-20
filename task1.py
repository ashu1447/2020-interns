import json
from dateutil import parser
import matplotlib.pyplot as plt 

with open('/content/data.json') as file:
    data = json.load(file)   
time1=parser.parse('2019-01-01')
time2=parser.parse('2019-01-31')
dates=[]
price=[]
for i in data['rates']:
    time3 = parser.parse(i)
    if time3 <= time2 and time3 >= time1:
        dates.append(i)
        price.append(data['rates'][i]['INR'])

map_data=list(zip(dates,price))
result = sorted(map_data, key = lambda x: x[0])
dates=[]
price=[]
dates,price = zip(*result)
plt.plot(dates,price)
plt.xlabel('Dates')
plt.xticks(rotation=90)
plt.ylabel('Rates of Jan 2019')
plt.title('Exchange rate of INR against EUR')
plt.show()