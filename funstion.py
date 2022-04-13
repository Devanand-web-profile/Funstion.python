'''  1. no return no parameter
 2. no return with parameter
 3. return without parameter
 4. rerturn with parameter
'''
# function is always used [ def ]
'''

# 1.


def welcome():
    print("this is a welcome function :")
def hello():
    print("hello functio ")
    welcome()
hello()

 
#  2.  no return withh parameter

def hello(x):       # (x) = parameter 
    print(x+x,x*2)
    
    
hello(12)   # argument passing
hello('ranchi')
hello([12,25,56])
hello((12,45,78))
hello(9,)
 
'''# pasing 2 parameter  '''
'''
def go(x,y):
    print(x+y)

go(9,4)
go("ranch ","jhar")



def hi(x=10):
    print(x+x)
hi(15)
hi()



def by(x,y=10):
    print(x+y)
by(4+3)
by(15)
'''
# 3.string argument with Parameter
    # Note : args value shoyld be change
'''
def hi(*args):
    print(args)
hi(54)
hi("hello",45,2.56)


# keyworded argument ....

def hi(*args):
    for x in args:
        print(x , end=" ")

hi(45)
hi(21,45,56)
hi1=("hello boy")
hi(*hi1)


def default(*args,code=1):
    print(args,code)

default(12)
default(24,code=1)
default([45,89,96], code=45)

'''
'''
#  Variable argument 
def hello(**kwargs):
    print(kwargs)

hello(name="ranjan")
hello(name="manoj",city="ranchi")
d={"name":"ranjeet","country":"india","city":"tata"}
hello(**d)
'''
'''
def hello(**kwargs):
    #for x in kwargs:
    #for x in kwargs.items():
    #for x in kwargs.keys():
    for x in kwargs.values():
        print(x)

hello(name="ranjan")
hello(name="manoj",city="ranchi")
d={"name":"ranjeet","country":"india","city":"tata"}
'''







