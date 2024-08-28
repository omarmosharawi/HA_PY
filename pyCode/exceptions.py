try:
    x = 5
    y = 0
    r = x / y
    print(f'{x}/{y}={r}')
except:
    print('Did you divide by zero?')



try:
    with open('file1.txt') as file:
        data = file.read()
except:
    print('Can not find the file')

try:
    with open('file3.txt', 'w') as file:
        x = 5
        y = 5
        r = x / y
        file.write(f'{x}/{y}={r}')
except FileNotFoundError as error:
    print(error)
except ZeroDivisionError as error: # we can use more than one except clause
    print(error)
else:
    print('The result was written to the file')
finally: # finally is always executed, even if there are exceptions or no exceptions at all
    print('Code executions was finished')
