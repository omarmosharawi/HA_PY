import re

# sub() function replaces matches with a string.
t = """Hello, my number is 476-597-1654
my friend number is 623-456-1694"""
replace = re.sub(r"\d{3}-\d{3}-\d{4}", "777 707 7070", t, 1)    # 1 this count that you want to replace. if count not exist will replace all attributes
print(replace)

print('-'*30)
# split() function is used to split text based on the given expression.
text = 'My name is Omar Mohamed'
s1 = re.split(r"\s", text)
print(s1)
s2 = re.split(r"\s", text, 3)
print(s2)