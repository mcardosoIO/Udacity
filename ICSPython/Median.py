# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
   if a > b:
      return a
   else:
      return b

def biggest(a,b,c):
   return bigger(a,bigger(b,c))

def small(a,b):
   if a > b:
      return b
   else:
      return a

def smaller(a,b,c):
   return small(a,small(b,c))

def median(a,b,c):
   biggestABC = biggest(a,b,c)
   #print('biggestABC: ', biggestABC) 
   smallerABC = smaller(a,b,c)
   #print('smallerABC', smallerABC)

   if a == biggest(a,b,c):
      if b == smaller(a,b,c):
         return c
      else:
         return b

   if b == biggest(a,b,c):
      if c == smaller(a,b,c):
         return a
      else:
         return c

   if c == biggest(a,b,c):
      if a == smaller(a,b,c):
         return b
      else:
         return a

print(median(1,3,2)) 
#>>> 2
print(median(1,2,3)) 
#>>> 2
print(median(2,2,1))
#>>> 2
print(median(9,3,6))
#>>> 6
print(median(7,8,7))
#>>> 7








