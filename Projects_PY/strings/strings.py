str1 = 'this is string one'
str2 = "this is string two"
print('1)', str1)
print('2)', str2)

str3 = 'this is string \"three\''   # to add (') or (") in the string type, use the backslash (\) before them
print('3)', str3)

str4 = "this is string 'four'"  # can use single quote (') in this ("") without using (\)
print('4)', str4)
str5 = 'this is string "five"'  # can use double quote (") in this ('') without using (\)
print('5)', str5)

numbers1 = "1\n2\n3"
print('6)', numbers1)   # will print 1 newline 2 newline 3

numbers2 = ("1"
            "2"
            "3")
print('7)', numbers2)   # will print 123

numbers3 = "1" \
    "2" \
    "3"
print('8)', numbers3)   # will print 123

numbers4 = """
1
2
3
"""
print('9)', numbers4)   # will print newline 1 newline 2 newline 3 newline

# => this use for single comment
""" 
 test
 test 
 test
"""    # (""" """) => this use for more than one line to comment



# Concatenation
print('10)', str1 + str2)
print('11)', str1 + ' ' + str2)



# Repeat
print('12)', str1 * 5)
print('13)', (str1 + ' ') * 5)
