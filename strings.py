#indexing

mystring = 'abcdefg'

print(mystring)

#grab single element
# -1 grabs last letter
print(mystring[-1])

#start from second then to end
print(mystring[2:])

#start from beginning then to certain point

print(mystring[:3])

#strings are imutable

# .upper method returns copy in upper case

x = mystring.capitalize()

print(x)


y = mystring.split('b')

print(y)

#print formatting

print('This is a string with a {p}' .format(p='insert'))
