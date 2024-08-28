# program 1
opNum = int(input('Enter stars number: '))

if opNum > 0:
    for i in range (1, opNum+1):
        print("* " * i)
else: print('please enter a valid number')



# program 2
for i in range (1, 6):
    if i == 3:
        print('* Omar Mohamed Sharawi  *')
        continue
    else: print('* '*13)



# program 3
num = 1
for i in range (0,5):
    for o in range (0,i+1):
        print(num, end = ' ')
        num += 1
    print()
