import json
import matplotlib.pyplot as plt
import requests
start_date = '2019-01-01'
end_date = '2019-03-31'
url='https://api.exchangeratesapi.io/history?start_at={}&end_at={}&symbols=INR,GBP'.format(start_date,end_date)
url2='https://api.exchangeratesapi.io/latest?symbols=INR,GBP'
response = requests.get(url)
file = response.text
data = json.loads(file)
response2 = requests.get(url2)
f = response2.text
latest_rates = json.loads(f)
dates=[]
price_INR = []
price_GBP = []
x_coord=0 
for i in data['rates']:
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
plt.figure(figsize=(20,20))

plt.plot(dates,price_INR, label='INR')
plt.plot(dates,price_GBP, label='GBP')
plt.annotate('INR curr_rate-'+str(latest_rates['rates']['INR']),
             (x_coord-5,y_coord),
             textcoords='offset points',
             xytext=(0,40),ha='center')
plt.annotate('GBP curr_rate-'+str(latest_rates['rates']['GBP']),
             (x_coord-5,y_coord),
             textcoords='offset points',
             xytext=(0,30),ha='center')
plt.xlabel('Dates in 2019')
plt.xticks(rotation=90)
plt.ylabel('Rates of  2019')
plt.title('Exchange rate against EUR')
plt.legend()
plt.show()