import re


def isEmail(email):
    isMail = re.search(r"^[A-z0-9]+[\.-]?[A-z0-9]+@\w+\.\w{2,3}$", email)

    if isMail:
        print(f'the {email} is valid')
    else:
        print(f'the {email} not valid')



isEmail('omarmosharawi.com')
isEmail('omarmosharawi@com')
isEmail('omarmosharawi@gmail.com')
isEmail('omarmosharawi@gmail')
isEmail('@omarmosharawi@gmail.com')
isEmail('OmarMoSharawi7@gmail.net')
isEmail('OmarMoSharawi7@gmail.net')
isEmail('omar.sharawi@gmail.com')