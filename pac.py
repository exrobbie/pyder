from enum import Enum

Weekdays = Enum('Weekdays', ('Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun'))

for x, y in Weekdays.__members__.items():
    print(x, y)
