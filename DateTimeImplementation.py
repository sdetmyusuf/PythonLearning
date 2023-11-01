import time, datetime

epocsec = time.time()
print(epocsec)#it will display in different format we will have to convert that into correct format using ctime() method

t = time.ctime(epocsec) #it will display the date, time year and day..
print(t)

dt = datetime.datetime.today()
print(dt)

# we can get different parts seprately like date, day and time etc as follows -

print(dt.day, dt.month,dt.year)
print('Current date formatted {}/{}/{}'.format(dt.day, dt.month,dt.year))
print(dt.hour, dt.minute,dt.second)
print('Current time formatted {}:{}:{}'.format(dt.hour, dt.minute,dt.second))
#--------------combine date and time--------------------------

day  = datetime.date(2023, 11, 1)
tim = datetime.time(12, 45, 56)

datetime.combine(day,tim)
