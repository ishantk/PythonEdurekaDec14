import datetime

today = datetime.datetime.today()
print(today)
print(type(today))

tomorrow = datetime.datetime(2019, 1, 1, 12, 12, 15)
print(tomorrow)

print(tomorrow-today)

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

time = datetime.time
timeZone = datetime.timezone

print(time)
print(type(time))

print(timeZone)
print(type(timeZone))

