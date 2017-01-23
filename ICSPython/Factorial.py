# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
   if n == 0:
      return 1
 
   resultado = 1
   while(n > 1):
      resultado = resultado * n
      n = n - 1
   return resultado


print factorial(0)
#>>> 1
print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720


