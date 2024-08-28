# app without using regular expressions

def isPhone(text):
    if len(text) != 12:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():     # isdecimal() function checks whether a string consists of numbers only.
            return False

    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True



print(isPhone('447-559-1111'))
print(isPhone('447-559-11115'))
print(isPhone('447-5599-1111'))