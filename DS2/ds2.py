"""x=5
name="Sam"
y=3.2
true=True
print(dir(name))#1
print(type(name))
print((type(x)))
print(type(y))
print(type(true))
print(name)
#name="Sam
print(help(str))#2
print(help(name.upper))#3
print(name.upper())
print(name)#4 Here value of name variable doesn't change with any method
upper=name.upper()
print(upper)
#5)don't name your file as the name of library on which you are vworking
print(dir())
#print(help())

for i in range(3):
    print(name)

for _ in range(3):
    print(name)

for i in range(3):
    print(i)

for i in range(1,5):
    print(i)

for i in range(2,11,1):
    print(i)

print(help(range))

#list
print(help(list()))
print(dir(list))

l_5=list(range(5))
print(l_5)
print(len(l_5))
print((type(l_5)))

for num in l_5:
    print(num)

for num in l_5:
    print(num)
    print("")
    print(num*2)
    print("")

for num in l_5:
    print(num)
    print(num*2)
    print("")

for l_5 in range(0,9):
    print(l_5)
print(l_5)#6) doubt here
print(help(len))

#Slicing
name='Samuel'
print(name[0])
print(name[0:4])

'''
S a m u e l
0 1 2 3 4 5
'''

print(name[:5])
print(name[:])
print(name[::2])
print(name[::1])
print(name[::-1])

name="Sam"
print(name[1:])
print("p"+name[:1])
print("p"+name[1:])

letters="ptjb"
for letter in letters:
    print(letter+name[1:])

#print(help())

def hello():
    print("Hello")
hello()

def hello(name):
    print("Hello "+name)
hello("Sam")

#Input Function
#print(help())
def hello():
    name=input("Enter your name\n")
    print("Hello "+name)
hello()

def blank():
    print()
def blank_3():
    blank()
    blank()
    blank()
def blank_9():
    blank_3()
    blank_3()
    blank_3()
blank_9()
"""
numbers=[1,5,2,4,6,10,3]
for number in numbers:
    print(number)

print(1==1)
print(1==0)

numbers=[1,5,2,4,6,10,3]
for number in numbers:
    if True:
        print(number)

numbers=[1,5,2,4,6,10,3]
for number in numbers:
    if number%2==0:
        print(number)

numbers=[1,5,2,4,6,10,3]
for number in numbers:
    if number%2==0:
        print(number,"is even")

numbers=[1,5,2,4,6,10,3]
for number in numbers:
    if False:
        print(number)

numbers=[1,5,2,4,6,10,3]
for number in numbers:
    if number%2==0:
        print(number,"is even")
    else:
        print(number,"is odd")

numbers=[1,-5,2,-4,6,-10,3]
for number in numbers:
    if number==0:
        print("zero")
    elif number>0:
        print("positive")
    else:
        print("negative")

def even(x):
    """enter number to be checked if even"""
    if x%2==0:
        return True
even(4)#do not print anything
print(even(4))

def even(x):
    return x%2==0
print(even(6))

def odd(y):
    return y%2!=0
print(odd(6))

for row in range(5):
    print(row)
    for col in range(5):
        print(col)

for row in range(5):
    print(row)
    for col in range(5):
        print(col,end='')

for row in range(5):
    for col in range(5):
        print(col,end='')

#print five row and five columns
for row in range(5):
    for col in range(5):
        print(col,end='')
    print()





