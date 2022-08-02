# import asyncio
# import time
#
#
# async def fun1(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print('fun1 завершена')
#
#
# async def fun2(x):
#     print(x**0.5)
#     await asyncio.sleep(3)
#     print('fun2 завершена')
#
#
# async def main():
#     task1 = asyncio.create_task(fun1(4))
#     task2 = asyncio.create_task(fun2(4))
#
#     await task1
#     await task2
#
#
# print(time.strftime('%X'))
#
# asyncio.run(main())
#
# print(time.strftime('%X'))

import requests
from bs4 import BeautifulSoup

url = 'https://m.myfin.by/currency/minsk'        # адрес мобильной версии
headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')

usd = soup.find('div', class_='bl_usd_ex').text  # тут котировки в div-ах,
eur = soup.find('div', class_='bl_eur_ex').text  # не span, как в десктопной

print(f'usd: {usd}, eur: {eur}')