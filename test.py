# import random
import os
import requests
# mem_for_choose = ['mem1.jpg', 'mem2.jpg', 'mem3.jpg']
# test = random.choice(mem_for_choose)
# print(test)

# directory = 'media'
# files = os.listdir('media')
# print(files)

url = 'https://api.exchangerate.host/latest'
response = requests.get(url)
# data = dict()
data = response.json()

# print(data)
# for k in data:
#     print(k)
date = data.get('date')
print(date)
print(data.get('rates', {}).get('KGS'))

