name = 'Omar'
age = 20
rank = 1.0

# print('My name is ' + name + ' and my age is ' + age)   # this will be error (can only concatenate str (not "int") to str)
print('My name is ' + name + ' and my age is ' + str(age))  # we must make int to str

print(f"I'm {name}, I'm {age} years old.")  # we can use f'' instead of converting int to str # the best method for using format string
print(f"I'm {name}, I'm {age+1} years old. My rank is {rank}")

print("I'm %s. I'm %d years old. My rank is %f" % (name, age, rank))    # (%s => string) / (%d => digit) / [(%f => float) - (%.3f => to control zero => .3f to print 3 number after(.) )]

print("I'm {}. I'm {} years old. My rank is {}".format(name, age, rank))    # another way by using format() function
print("I'm {:s}. I'm {:d} years old. My rank is {:.3f}".format(name, age, rank))
print("I'm {0}. I'm {1} years old. My rank is {2}".format(name, age, rank))     # {} by number of index
print("I'm {n}. I'm {a} years old. My rank is {r}".format(n=name, a=age, r=rank))   # by using keys