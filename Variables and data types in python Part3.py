# Example variable declarations
x = 22
name = "John Doe"
is_valid = True

print(x,name,is_valid)

#Python data types

x = 42         # integer
y = 3.14       # float
z = 1 + 2j     # complex

#Strings

name = "John Doe"
message = 'Hello, World!'

#Boolean

is_true = True
is_false = False

#Bytes in Python 

my_byte = b'Hello'
my_string = my_byte.decode('utf-8')  # converts bytes to a string using UTF-8 encoding
print(my_string)  # 'Hello'

new_byte = my_string.encode('utf-8')  # converts the string back to bytes using UTF-8 encoding
print(new_byte)  # b'Hello'

#List in Python

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])  # 'apple'
print(my_list[-1])  # 'cherry'

#Tuples in Python 

my_tuple = (1, 2, 3, 4, 5)  # a tuple of integers
print(my_tuple)  # (1, 2, 3, 4, 5)

my_tuple2 = ('apple', 'banana', 'cherry')  # a tuple of strings
print(my_tuple2)  # ('apple', 'banana', 'cherry')

my_tuple3 = (1, 'apple', True, 3.14)  # a tuple with mixed data types
print(my_tuple3)  # (1, 'apple', True, 3.14)
