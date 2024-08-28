import quotes, sys #1
import quotes as q #4
from quotes import get_quotes #2
from quotes import * #3 # (*) this mean import all file # this method not recommended to make it more clear and easy to read
from quotes import get_quotes as qts #3 # as used to rename the function

print(quotes.get_quotes()) #1 # use function that in quotes file to get a quote from the list of quotes # from import all file
print(q.get_quotes()) #4
print(get_quotes()) #2 #3 # from the module "quotes"
print(qts()) #3

print(sys.path) # print out the current system path - useful for debugging when you're not sure where your code is coming from



def get_q():
    try:
        import quotes as qt     # can not use (import *) in functions
    except:
        print('Error importing, quotes package may be missing')
        return None
    else:
        quote = qt.get_quotes()
        return f'The quotes are:\n{quote}'

print(get_q())
