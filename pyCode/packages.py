import myPackage.module1 as m1, myPackage.module2 as m2 # importing modules from folders
# from myPackage import module1, module2 # another way to import modules from folders
# after create a new file named "__init__.py" in the same directory with module1 and module2 files will print the lines have been defined in this file

m1.mdl1()
m2.mdl2()



# after create '__init__.py'
import myPackage
print(myPackage.__file__)   # it will print the path of __init__.py file in the package folder
myPackage.module1.mdl1()
myPackage.module2.mdl2()



# we can use sub packages also like this:
import myPackage.subPackage.module3 as m3
m3.mdl3()



print(dir())   # list all names currently defined in this Python interpreter session
from myPackage import *
print(dir())   # now it lists everything that is available in 'myPackage'
