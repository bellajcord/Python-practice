# Logical operators

# and
(1 > 2) and (2 < 3)

# multiple

(1 == 2) or (2 == 3) or (4 == 4)

##################################
### if,elif, else Statements #####
##################################

# Indentation is extremely important in Python and is basically Python's way of
# getting rid of enclosing brackets like {} we've seen in the past and are common
# with other languages. This adds to Python's readability and is huge part of the
# "Zen of Python". It is also a big reason why its so popular for beginners. Any
# text editor or IDE should be able to auto-indent for you, but always double check
# this if you ever get errors in your code! Code blocks are then noted by a colon (:).

if 1 < 2:
    print('yep')

if 1 < 2:
    print('first')
else:
    print('last')

# To add more conditions (like else if) you just use a single phrase "elif"

if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('last')


#loops

 # Time to review loops with Python, such as For Loops and While loops
# Python is unique in that is discards parenthesis and brackets in favor of a
# whitespace system that defines blocks of code through indentation, this forces
# the user to write readable code, which is great for future you looking back at
# your older code later on!


# loop with list

seq = [1,2,3,4,5]

for item in seq:
    print(item)

# Perform an action for every element but doesn't actually involve the elements

for item in seq:
    print('yep')

# You can call the loop variable whatever you want:

for jelly in seq:
    print(jelly+jelly)

## For Loop with a Dictionary

ages = {"sam":3, "Frank":2, "Dan":4}

for key in ages:
    print("This is the key")
    print(key)
    print("this is the value")
    print(ages[key])

# A list of tuple pairs is a very common format for functions to return data in
# Because it is so common we can use tuple un-packing to deal with this, example:

mypairs = [(1,10),(3,30),(5,50)]

#normal
for tup in mypairs:
    print(tup)

#unpacking

for item1, item2 in mypairs:
    print(item1)
    print(item2)

#######################
### WHILE LOOPS #######
#######################

# While loops allow us to continually perform and action until a condition
# becomes true. For example:

i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1

# RANGE FUNCTION
# range() can quickly generate integers for you, based on a starting and ending point

# Note that its a generator:

range(5)

list(range(5))

for i in range(5):
    print(i)

# List Comprehension
# This technique allows you to quickly create lists with a single line of code.
# You can think of this as deconstructing a for loop with an append(). For Example:

x = [1,2,3,4]

out = []
for item in x:
    out.append(item**2)
print(out)

#writen in list comp form

[item**2 for item in x]