employee = {
    'name': 'Omar',
    'BD': '27 Jul 2003',
    'position': 'Software Engineer'
}
print(employee)

employees = {
    1: {'name': 'Omar', 'age': 20, 'title': 'Software Engineer', 'salary': '30$ per h'},
    2: {'name': 'Ahmed', 'age': 19, 'title': 'Software Engineer', 'salary': '10$ per h'},
    3: {'name': 'Mariam', 'age': 17, 'title': 'Software Engineer', 'salary': '15$ per h'}
}
print(employees)

progLang = {
    'frontEnd': {
        1: 'HTML',
        2: 'CSS',
        3: 'JS'
    },
    'backEnd': {
        1: 'Node JS',
        2: 'PHP',
        3: 'python',
        4: 'SQl',
    }
}
print(progLang)

print('-'*30)
# items() function returns a new return of the dictionary items in the form (key, value) => tuple.
print(employee.items())
print(employees.items())
print(progLang.items())

print('-'*30)
# keys() function returns a new view containing all the keys of the dictionary.
print(employee.keys())
print(employees.keys())
print(progLang.keys())

print('-'*30)
# values() function is used to display key values for a dictionary.
print(employee.values())
print(employees.values())
print(progLang.values())