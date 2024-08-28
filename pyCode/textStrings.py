name = 'Omar Mohamed'
print('1)', name)
print('2)', 'omar' in name)
print('3)', 'Omar' in name)
print('4)', name[0],name[1],name[2],name[3])
print('5)', name[-12],name[-11],name[-10], name[-9])
print('6)', len(name))
print('7)', 'm' in name)
print('8)', 'H' in name)

name2 = 'omar mohamed'
name2 = name2.capitalize() # capitalize() method converts the first character of each word to a capital letter
print('9)', name2)



print('10)', name2.split()) # split the string into a list of words # by default it splits at space
print("11)", name2.upper()) # convert all letters to uppercase
print("12)", name2.lower()) # convert all letters to lowercase

# find methods by index # index method used to do the same like find method but instead of return false will return an error msg
print('13)', name2.find('O'))
print('14)', name2.find('o'))
# find methods return -1 if not found, so we add +1 to get the correct index
print("15) First occurrence of 'a': ", name2.find('a')+1)
print("16) Last occurrence of 'a': ", name2.rfind('a')+1)

# slicing [start:stop] stop is exclusive, [start:stop:step] step is how much you move each time
# : means that we are skipping certain number of steps
print("17) Characters from second last character till end: ", name2[-2:])
print("18) All characters after first occurrence of 'a': ", name2[name2.find('r')+1:])
print("19) Characters between first and last 'a'", name2[:name2.find('a')]+name2[(name2.rfind('a'))+1:])

print('20)', name2.endswith('med')) # endswith check the last characters
print('21)', name2.endswith('dem'))



names = ['omar','mohamed','ahmed','abdullah','ali']
print('22)', names[0]+', ' + names[1]+', ' + names[2]+', ' + names[3]+', ' + names[4])
# another method to make the same thing # called join()
spaces = ', '
namesSpaces = spaces.join(names)
print('23)', namesSpaces)
print('25)', names) # printed as a list



# format method can be used with any object but it works best with strings
msg = 'Hello, {}'
nameInput = str(input('Enter Your Name: '))
format_msg = msg.format(nameInput) # format takes variables inside curly brackets {} and put them in place of the variable
print('26)', format_msg)

print('27)', '{0}, {1}, {2}'.format('a', 'b', 'c'))
print('28)', '{2}, {1}, {0}'.format('a', 'b', 'c'))
# print('27)', '{1}, {2}, {3}'.format('a', 'b', 'c')) # this an error because it will look for wrong index arrangement

progLang = 'Languages: {one}, {two}, {three}'.format(one='Python', two='Java', three='C++')
print('29)', progLang)

print('30)', f'Hello, {names[0]}') # f method is a another way to make a string format 
