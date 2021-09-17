# similar to arrays

mylist= [1,2,3]

varlist = ['A string', 2,100,123, '0']

len(mylist)

#indexing and slicing

my_list = ['one','two','three',4,5]

# use + to concatinate

mylist +  ['new item']

#add permenant

my_list = my_list + ['new item is perm']
#

#duplicate list

my_list * 2

# append, add item to end of list

my_list.append('append me')

#pop removes last item

my_list.pop(0)

# reverse item

my_list.reverse()

#sort alphabetical or ascending

my_list.sort()

# nested list

lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

matrix = [lst_1,lst_2,lst_3]

#grab first itme in matrix object
matrix[0]

# grab first item in first item in matrix
matrix[0][0]

#list comprehension

# Python has an advanced feature called list comprehensions. They allow for
# quick construction of lists. To fully understand list comprehensions we need
# to understand for loops. So don't worry if you don't completely understand
# this section, and feel free to just skip it since we will return to this topic later.
#
# But in case you want to know now, here are a few examples!

# Build a list comprehension by deconstructing a for loop within a []

first_col = [row[0] for row in matrix]


