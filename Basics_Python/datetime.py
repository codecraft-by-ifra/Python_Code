import datetime

Interval = datetime.datetime.now()
print(f'Date and Time  : {Interval}')

Date = datetime.date.today()
print(f'Today Date is : {Date}')

Time = datetime.datetime.now()
print(f'Time is now : {Time.time()}')





#camelcase
from camelcase import CamelCase
c = CamelCase()
print(c.hump('heloo its an big day'))


