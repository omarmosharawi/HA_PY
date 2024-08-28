list = ['Omar', 'Mohamed', 'Hussien']
print(' '.join(list))   # join() => returns the string resulting from joining the strings of an iterable objects
print('_'.join(list))
print(' & '.join(list))

print('-'*15)

t = 'Omar Mohamed Hussien Ali'
print(t.split())    # split() => splits a string into a list of strings based on a specified separator
print(t.split('  '))

t = 'Omar_Mohamed_Hussien_Ali'
print(t.split())    # split() => splits a string into a list of strings based on a specified separator
print(t.split('_'))

t = '''Omar
Mohamed Hussien
Ali'''
print(t)
print(t.split('\n'))    # split() => splits a string into a list of strings based on a specified separator
print(t.splitlines())   # splitlines() => splits a string into a list of strings based on a new line

t = 'Omar\nMohamed Hussien\nAli'
print(t)
print(t.splitlines())   # splitlines() => splits a string into a list of strings based on a new line
