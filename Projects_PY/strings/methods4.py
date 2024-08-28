t = 'Welcome'

print(t)

print(t.rjust(15))   # Return a right-justified string of length width. Padding is done using the specified fill character (default is a space).
print(t.ljust(15))   # Return a left-justified string of length width. Padding is done using the specified fill character (default is a space).
print(t.center(15))  # Return a centered string of length width. Padding is done using the specified fill character (default is a space).

print(t.rjust(11, '#'))     # will replace spaces by char
print(t.ljust(11, '#'))     # will replace spaces by char
print(t.center(11, '#'))    # will replace spaces by char



n = 'Omar\tMohamed Hussien\tAli'
print(n.expandtabs(1))  # Return a copy where all tab characters are expanded using spaces. If tabsize is not given, a tab size of 8 characters is assumed.
