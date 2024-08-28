# calculate student grade

inputGrade = int(input('Enter student grades: '))

# if inputGrade > 0:
#     if inputGrade >= 90 and inputGrade <= 100:
#         print('the student got A')
#     elif inputGrade >= 80 and inputGrade <= 89:
#         print('the student got B')
#     elif inputGrade >= 70 and inputGrade <= 79:
#         print('the student got C')
#     elif inputGrade >= 60 and inputGrade <= 69:
#         print('the student got D')
#     elif inputGrade >= 50 and inputGrade <= 59:
#         print('the student got E')
#     elif inputGrade >= 0 and inputGrade <= 49:
#         print('the student got F')
#     else: print('please enter a valid number')
# else: print('please enter a positive number (greater than zero)')

if inputGrade > 0:
    if inputGrade in range (90,101):
        print('the student got A')
    elif inputGrade in range (80,90):
        print('the student got B')
    elif inputGrade in range (70,80):
        print('the student got C')
    elif inputGrade in range (60,70):
        print('the student got D')
    elif inputGrade in range (50,60):
        print('the student got E')
    elif inputGrade in range (0,50):
        print('the student got F')
    else: print('please enter a valid number')
else: print('please enter a positive number (greater than zero)')
