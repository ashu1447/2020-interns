import json
from dateutil import parser
import matplotlib.pyplot as plt 
with open('/content/data.json') as file:
    data = json.load(file)
with open('/content/latest-rates.json') as f:
    latest_rates = json.load(f)    
time1=parser.parse('2019-01-01')
time2=parser.parse('2019-01-31')
dates=[]
price_INR = []
price_GBP = []
x_coord=0 
for i in data['rates']:
    time3 = parser.parse(i)
    if time3 <= time2 and time3 >= time1:
        dates.append(i)
        price_INR.append(data['rates'][i]['INR'])
        price_GBP.append(data['rates'][i]['GBP'])
        x_coord += 1
map_data=list(zip(dates,price_INR,price_GBP))
result = sorted(map_data, key = lambda x: x[0])
dates.clear()
price_INR.clear()
price_GBP.clear()
dates, price_INR, price_GBP = zip(*result)
a=max(price_INR)
b=max(price_GBP)
y_coord=max(a,b)
plt.plot(dates,price_INR, label='INR')
plt.plot(dates,price_GBP, label='GBP')
plt.annotate('INR current rate-'+str(latest_rates['rates']['INR']),
             (x_coord-5,y_coord),
             textcoords='offset points',
             xytext=(0,40),ha='center')
plt.annotate('GBP current rate-'+str(latest_rates['rates']['GBP']),
             (x_coord-5,y_coord),
             textcoords='offset points',
             xytext=(0,30),ha='center')
plt.xlabel('Dates in Jan 2019')
plt.xticks(rotation=90)
plt.ylabel('Rates of Jan 2019')
plt.title('Exchange rate against EUR')
plt.legend()
plt.show()