# app using regular expressions

import re


def isPhone(text):
    is_phone = re.search(r"\d{3}-\d{3}-\d{4}", text)

    if is_phone:
        print(f'the {text} is valid')
    else:
        print(f'the {text} is not valid')



print(isPhone('447-559-1111'))
print(isPhone('447-559-11115'))
print(isPhone('447-5599-1111'))