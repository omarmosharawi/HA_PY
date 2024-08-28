# a program to flip words into a text string

s = 'Hello Im Omar Mohamed as a Software Engineer'

l = s.split(' ')
l.reverse()

afterRev = ' '.join(l)

print(afterRev)