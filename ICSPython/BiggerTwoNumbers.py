# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.



def bigger(x,y):
   if (x > y):
      return x
   if (x < y):
      return y
   if (x == y):
      return x

def bigger2(x,y):
    if (x > y):
        return x
    return y

def bigger3(x,y):
   if (x > y):
      return x
   else:
      return y



print 'bigger procedure'
print bigger(2,7)
#>>> 7

print bigger(3,2)
#>>> 3

print bigger(3,3)
#>>> 3


print 'bigger2 procedure'
print bigger2(2,7)
#>>> 7

print bigger2(3,2)
#>>> 3

print bigger2(3,3)
#>>> 3


print 'bigger3 procedure'
print bigger3(2,7)
#>>> 7

print bigger3(3,2)
#>>> 3

print bigger3(3,3)
#>>> 3
