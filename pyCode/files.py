# f = open('file.txt', 'w') # 'w' used to write in the file
f = open('C:\\Users\\Omar Mohamed\\Desktop\\pyCode\\file.txt', 'w') # this way you can specify the path of your file
f.write('Welcome in my system') # write to the file, append at end of file
f.write('\nPowered by Omar Mohamed')
f.close() # close the file # no operations can be performed on a closed file or after the file has closed

f = open('C:\\Users\\Omar Mohamed\\Desktop\\pyCode\\file.txt', 'r') # 'r' is for read mode
print(f.read()) # print all content from the file
f.close()
# another way to print all file using loop
f = open('C:\\Users\\Omar Mohamed\\Desktop\\pyCode\\file.txt', 'r')
for lines in f:
    print('\n', lines, end=' ')
f.close()

f = open('C:\\Users\\Omar Mohamed\\Desktop\\pyCode\\file.txt', 'r')
print('\nthe first 7 characters:', f.read(7)) # print 10 characters from the start of the file
f.close()

f = open('C:\\Users\\Omar Mohamed\\Desktop\\pyCode\\file.txt', 'r')
print('\nthe first line:', f.readline()) # print  one line (until \n) and move the cursor to next line # when we pass a parameter in readline function it will be move in a specific position
print('the second line:', f.readline()) # reads until it encounters '\n' and returns everything till that point
f.close()



# another way to open and read the file
with open('C:\\Users\\Omar Mohamed\\Desktop\\pyCode\\file.txt', 'a') as f: # 'a' used to add/append data into the file
    f.write('\nThis is written inside with block\n')

with open('C:\\Users\\Omar Mohamed\\Desktop\\pyCode\\file.txt') as f:
    print(f.read())



# open multiple files at once and move data between them
with open('C:\\Users\\Omar Mohamed\\Desktop\\pyCode\\file.txt', 'r') as f, open('C:\\Users\\Omar Mohamed\\Desktop\\pyCode\\file2.txt', 'a') as f2:
    f_lines = f.read()
    f2.write(f_lines)



# open images file types
with open('C:\\Users\\Omar Mohamed\\Desktop\\pyCode\\img.png', 'rb') as I:
    print(I.read(7)) # will print bytes not string



# exception handling while reading/writing files
try:
    f = open('C:\\Users\\Omar Mohamed\\Desktop\\pyCode\\notExistFile.txt', 'r')
except FileNotFoundError:
    print("Sorry, the file does not exist")
else:
    print("The file exists")
