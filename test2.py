from datetime import datetime

import time
#
# a = 2
# for i in range(10):
#     b = f'item item-day-{a} link date-left'
#     print(a)
#     print(b)
#     a += 1

today = datetime.today().date()
print(today)



# def fun1(x):
#     print(x**2)
#     time.sleep(3)
#     print('fun1 завершена')
#
#
# def fun2(x):
#     print(x**0.5)
#     time.sleep(3)
#     print('fun2 завершена')
#
#
# def main():
#     fun1(4)
#     fun2(4)
#
#
# print(time.strftime('%X'))
#
# main()
#
# now = datetime.now()
# after_1_minute = now + timedelta(minutes=0.1)
#
# print(now)
# print(after_1_minute)