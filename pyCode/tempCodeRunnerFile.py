1 # use function that in quotes file to get a quote from the list of quotes # from import all file
# print(q.get_quotes()) #4
# print(get_quotes()) #2 #3 # from the module "quotes"
# print(qts()) #3

# print(sys.path) # print out the current system path - useful for debugging when you're not sure where your code is coming from



# def get_q():
#     try:
#         import quotes as qt     # can not use (import *) in functions
#     except:
#         print('Error importing, quotes package may be missing')
#         return None
#     else:
#         quote = qt.get_quotes()
#         return f'The quotes are:\n{quote}'

# print(get_q())