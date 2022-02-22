## NUMBER 1
# 'del': We use the del() function is primarily used to delete objects

# Ex:
# assign variables 
my_variable1 = 20
my_variable2 = "GeeksForGeeks"

# delete both the variables
del my_variable1
del my_variable2

## NUMBER 2
#'pass': is a statement that is generally used as a placeholder i.e. when the user does not know what code to write.
# The pass statement is a null statement. 

# Ex:
a = 10
b = 20

if(a<b):
   pass
else:
   print("b<a")

## NUMBER 3
# 'max()': With a single iterable argument, return its biggest item. this returns the maximum value in a list.  

# Ex: 
list_of_integers = [55, 4, 92, 1, 104, 64, 73, 99, 20]
max_value = max(numbers)
print('Maximum value:', max_value) -> Maximum value: 104

## Number 4
# sorted: this function sorts the elements of a given iterable in a specific order (ascending or descending) and returns it as a list.
# Ex:
  
numbers = [4, 2, 12, 8]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# Output: [2, 4, 8, 12]  

## Number 5
# 'tuple': is an ordered collection of items.tuples are immutable (elements of a tuple cannot be changed). To create a tuple, we need to wrap items inside parentheses () and separate items by a comma.'''
# Ex:
list_of_numbers = (30, -5, 16, 19)
print(list_of_numbers)
