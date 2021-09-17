# def statements

def my_func(param1='default'):
    #anything in here belongs to scope of function
    print(param1)


# We can expand on this by using the return keyword, that way we can actually return
# a result and save it for future use, instead of just displaying it. Notice the
# lack of parenthesis or brackets, this is the power of whitespace!

def giveMeHello():
    return "hello"

result = giveMeHello()
print(result)

 #Let's write a function that returns tells you whether a number is even or not

def evenCheck(num):
     print("I'm checking to see if {} is even!".format(num))
     print(num%2 == 0)
evenCheck(41)

#Let's write a function that will add two numbers together, only if they are even!

def addEvenOnly(num1,num2):
    
    if(num1 % 2!=0) or (num2 % 2 != 0):
        return False
    else:
        return num1 + num2

# ######################
# Lambda Expressions
# ######################

#  You won't always need a full blown function, often you will just want to use
#  a function only once, in some of these cases, it makes more sense to use a
# lambda expression, also known as an anonymous function. Let's see an example:

def timesTwo(num):
    return num*2

#lambda expression

lambda num: num*2

# To really understand the use case for this, we need to introduce a function
# that accepts other functions as input parameters, in this case, we will use filter:

my_list = [1,2,3,4,5,6,7,8,9,10]

def evenBool(num):
    return num%2 == 0

evens = filter(evenBool, my_list)
print(list(evens))

#now with lambda

evens = filter(lambda num: num%2==0,my_list)
print(list(evens))

# Methods are almost like functions that are built into the object. Some Methods
# return something, others just affect the object in place. Later on in the OOP
# section we will learn how to create our own methods. For now, here are some
# useful common ones (this may be review)

st = 'hello my name is Sam'
st.lower()
st.upper()
st.split()

tweet = 'Go Sports! #Sports'
tweet.split('#')
tweet.split('#')[1]

d = {'k1':1,'k2':2}
d.keys()
d.items()

lst = [1,2,3]
x = lst.pop()

# in Operator (not a method, just something useful) boolean 
'x' in [1,2,3]
'x' in ['x','y','z']
