t1 = 'Welcome to New System'
print(t1.startswith('welcome'))      # startswith() function => check that the sentence begins with (value or char) and return boolean
print(t1.startswith('W'))
print(t1.startswith('N', 11, 20))   # startswith(value, start:IndexNumber, end:IndexNumber)
print(t1.endswith('System'))         # endswith() function => check that the sentence ends with (value or char) and return boolean
print(t1.endswith('s'))

print('-'*10)

t2 = '      Omar Mohamed      '
print(t2)
print(t2.strip())   # strip() => remove any spaces by default
print(t2.rstrip())  # rstrip() => remove any spaces from right by default
print(t2.lstrip())  # lstrip() => remove any spaces from left by default

print('-'*10)

t3 = '@omarmosharawi@'
print(t3.strip('@'))    # will remove the char from left and right
print(t3.rstrip('@'))   # will remove the char from the right

print('-'*10)

t4 = '#$%@omarmosharawi#'
print(t4.strip('#$%'))    # will remove any char from left and right
print(t4.rstrip('@#'))   # will remove the char from the right



print('-'*10)

hour = '1'
min = '7'
sec = '15'
milisec = '11'
print(f'{hour}:{min}:{sec}:{milisec}')
print(f'{hour.zfill(2)}:{min.zfill(2)}:{sec.zfill(2)}:{milisec.zfill(5)}')  # zfill(value) => value = number of indexes and completed it with zero from the left of string
