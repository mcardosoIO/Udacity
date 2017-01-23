# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.

def biggest(x,y,z):
   return bigger(x, bigger(y,z))

def bigger(y,z):
   if y > z:
      return y
   else:
      return z

def small(y,z):
   if y > z:
      return z
   else:
      return y

def smaller(x,y,z):
   return small(x, small(y,z))

def set_range(a,b,c):
   maximum = biggest(a,b,c)
   print maximum

def set_range(x,y,z):
   return biggest(x,y,z) - smaller(x,y,z)

print biggest(10, 4, 7)
print smaller(10, 4, 7)


print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

#print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6
