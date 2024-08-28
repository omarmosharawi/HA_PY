t = 'Powered by Omar Mohamed'
print(t)
print('-'*15)

print(t.index('Omar'))  # Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation. Raises ValueError when the substring is not found.
print(t.index('O'))
print(t.index('O', 0, 12))  # index(sub, start, end)
try:
    print(t.index('O', 0, 11))
except ValueError:
    print('Not found')

print('-'*15)

print(t.find('O', 0, 15))
print(t.find('O', 0, 11))   # Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.

print('-'*15)

x = 'one plus one plus one equal three'
print(x)

print(x.replace('one', '1'))               # replace() => will replace the str to another str
print(x.replace('one', '1', 1))     # replace(old, new, count of number do you want to replace)
