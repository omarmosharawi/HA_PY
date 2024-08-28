import re

phone = '415-430-7050'
s = re.search(r"(\d{3})-(\d{3})-(\d{4})", phone)
print(s.group())
print(s.group(0))
print(s.group(1))
print(s.group(2))
print(s.group(3))

print('-'*30)
date = '27-07-2003'
s = re.search(r"(\d{2})-(\d{2})-(\d{4})", date)
print(s)
print(s.group())
day = s.group(1)
month = s.group(2)
year = s.group(3)
print(f'{day}/{month}/{year}')
# .groups() used for multi values
day, month, year = s.groups()
print(f'{day}/{month}/{year}')