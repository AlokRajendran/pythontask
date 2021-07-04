
#FILTER

'''
marks = [40,45,43,44,49]

def greater(m):
        return m > 43
x = list(filter(greater, marks))
print(x)
'''

#MAP

'''
f = ["apple", "grapes", "banana"]

x = list(map(str.upper, f))
print(x)
'''


#DECORATORS  #to  modify existing func()

'''
def div(a,b):
    print(a/b)
    
def decorator(func):
    
    def new(a,b):
        
        if a>b:
            a,b = b,a
            return func(a,b)
    return new
div = decorator(div)
div(4,2)
'''

#DATE

import datetime

x = datetime.date.today()
print(x)


y = datetime.datetime.now()
print(y)

#to find year
print(y.year)

#to find day
print(y.strftime("%A"))

#to find day in short
print(y.strftime("%a"))

#day order
print(y.strftime("%w"))

#date only
print(y.strftime("%d"))

#month short
print(y.strftime("%b"))

#month
print(y.strftime("%B"))

#month number
print(y.strftime("%m"))

#hour
print(y.strftime("%h"))

#AM or PM
print(y.strftime("%p"))

#
print(y.strftime("%x"))

#time
print(y.strftime("%X"))

#year
print(y.strftime("%Y"))
