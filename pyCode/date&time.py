from datetime import date

wc2022 = date(2022, 11, 21)
print('1)', wc2022)

print('2)', date.today())

print('3)', date.fromordinal(738955)) # will print the date for ordinal day 738955

wcDate = date.fromisoformat('2026-07-01') # fromisoformat() method to convert ISO format (YYYY-MM-DD) to date object # An ordinal number is a count of days # Note: Python's "date" object # Note: this is not a valid date in # Note: The number of days since January
print('4)', wcDate)
print('5)', wcDate.year) # will return only year part of the date object

todayToWC = wcDate - date.today()
print('6)', todayToWC)
print('7)', type(todayToWC))



from datetime import time

time1 = time(10, 30, 45, 3000)
print('8)', time1)

time2 = time.fromisoformat('10:30:45')
print('9)', time2)



from datetime import datetime

WC2022 = datetime(year=2022, month=11, day=21, hour=13, minute=0, second=0, microsecond=0)
print('10)', WC2022)

print('11)', datetime.now())
print('12)', datetime.today())

WC_2022 = datetime.fromisoformat('2022-11-21 13:00:00')
print('13)', WC_2022)



from datetime import timedelta

td = timedelta(weeks=7, days=3, hours=15, minutes=30, seconds=10)
print('14)', td)

now = datetime.now()
print('15)', now + td)
print('16)', now.strftime('%A, %d%B-%Y')) # format date to string in way what you like
print('17)', now.strftime('%A, %d %B %Y'))
