# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_element(numbers, where):
   if where in numbers:
      return numbers.index(where)
   else:
      return -1

def find_element_other_way(numbers, where):
   if where not in numbers:
      return -1
   else:
      return numbers.index(where)



print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1



print find_element_other_way([1,2,3],3)
#>>> 2

print find_element_other_way(['alpha','beta'],'gamma')
#>>> -1
