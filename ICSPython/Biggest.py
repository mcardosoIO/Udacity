# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(x,y,z):
   return bigger(x, bigger(y,z))


def bigger(y,z):
   if y > z:
      return y
   else:
      return z


print 'bigger: ' + str(bigger(9, 9))



print 'biggest'
print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 6)
#>>> 9

print biggest(9, 3, 9)
#>>> 9
