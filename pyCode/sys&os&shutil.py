print('sys part:')

import sys

print('1)', sys.argv)          # list of command line arguments passed to script (argc in C)
print('2)', sys.platform)      # operating system
print('3)', sys.version_info)  # python version information

if sys.platform.startswith('win'):
    print("4) This is a Windows platform")
elif sys.platform.startswith('darwin'):
    print('4) This is a macOS platform')
elif sys.platform.startswith('linux'):
    print('4) This is a Linux platform')

if sys.version.startswith('3.9.5'):
    print("5) Python is up to date. Good job!")
else:
    print('5) Python is old. Please update!')

print('6)', sys.getwindowsversion()) # only on windows, returns tuple with info about the OS



print('='*50)
print('os part:')

import os

print(f'7) Current Working Directory: {os.getcwd()}') # get the current working directory
# os.chdir(r"..")                                       # change the current working directory .. move to back
# print(f'8) Current Working Directory after changing1: {os.getcwd()}')
# os.chdir('../pyCoding')                               # another way to go back one and move to another folder
# print(f'9) Current Working Directory after changing2: {os.getcwd()}')
# os.chdir(r"C:\Users\Omar Mohamed")                    # change the directory to this path
# print(f'10) Current Working Directory after changing3: {os.getcwd()}')

print('11)', os.listdir())    # list all files and directories in the current working directory

# another way to print list of dir
for file in os.listdir():   # iterate over each item in the list returned by os.listdir()
    if os.path.isfile(file):     # check if it's a file
        print(f'12) A file named "{file}" exists here.')

# another way to print all files in dir
alldir = os.scandir()        # return an iterator of os.DirEntry objects for the entries in the directory
for item in alldir:
    if item.is_file():
        print('13)', item.name)

# create file
try:
    os.mkdir('newFolder') # mkdir() function creates new folder
    print('14) newFolder created successfully.')
except FileExistsError as e:
    print('14)', e)

try:
    os.makedirs('newFolder/folder1') # makedirs() function creates new folders including parent folders if they don’t exist
    print('15) folder1 created successfully.')
except FileExistsError as e:
    print('15)', e)

os.rename('newFolder','testFolder') # rename 'newFolder' to 'testFolder'
os.rmdir('newFolder/folder1')       # remove only empty directory testFolder/folder1



print('='*50)
print('shutil part:')

import shutil

shutil.rmtree('newFolder/folder1')   # rmtree() method removes a directory even if it’s not empty

shutil.copy('requiremeents.txt', 'newFolder/folder1')  # copy() file from one place to another
shutil.copy2('requiremeents.txt', 'newFolder/folder1') # copy2() is like copy(), but also attempts to preserve file metadata (like permissions)

shutil.move('requiremeents.txt', 'newFolder/folder1')  # move() is like copy(), but delete original file
shutil.move('requiremeents.txt', 'newFolder/folder3')  # if destination already exist, raise error
