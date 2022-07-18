# # import random
# import os
import requests
# import python_weather
# import asyncio
#
#
# async def getweather():
#   # declare the client. format defaults to the metric system (celcius, km/h, etc.)
#   client = python_weather.Client(format=python_weather.IMPERIAL)
#
#   # fetch a weather forecast from a city
#   weather = await client.find("New York")
#   print(weather)
#
#   # returns the current day's forecast temperature (int)
#   current_t = (weather.current.temperature - 32)/1.8
#   # print(f'Current temperaure in Bishkek is {round(current_t, 1)} °C')
#
#   # get the weather forecast for a few days
#   for forecast in weather.forecasts:
#       date = str(forecast.date)
#       date = date[:11]
#       print(date, forecast.sky_text, round((forecast.temperature - 32) / 1.8, 1))
#
#   # close the wrapper once done
#   await client.close()
#   return f'Current temperaure in Bishkek is {round(current_t, 1)} °C'
#
# # if __name__ == "__main__":
#   # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
#   # for more details
#   # if os.name == "nt":
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#
# print(asyncio.run(getweather()))




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
print(data)
print(data.get('rates', {}).get('KGS'))
