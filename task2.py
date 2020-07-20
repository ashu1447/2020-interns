from dateutil import parser
import matplotlib.pyplot as plt 
import json
with open('/content/data.json') as file:
    data = json.load(file)    
time1=parser.parse('2019-01-01')
time2=parser.parse('2019-01-31')
dates=[]
price_INR = []
price_GBP = []
for i in data['rates']:
    time3 = parser.parse(i)
    if time3 <= time2 and time3 >= t1:
        dates.append(i)
        price_INR.append(data['rates'][i]['INR'])
        price_GBP.append(data['rates'][i]['GBP'])
map_data=list(zip(dates,price_INR,price_GBP))
result = sorted(map_data, key = lambda x: x[0])
dates.clear()
price_INR.clear()
price_GBP.clear()
dates, price_INR, price_GBP = zip(*result)
plt.plot(dates,price_INR, label='INR')
plt.plot(dates,price_GBP, label='GBP')
plt.xlabel('Dates in Jan 2019')
plt.xticks(rotation=90)
plt.ylabel('Rates of Jan 2019')
plt.title('Exchange rate og INR and GBP against EUR')
plt.legend()
plt.show()