# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

def is_friend(name):
   if name[0] == 'D':
      return True
   else: 
      if name[0] == 'N':
         return True
   return False

def is_friend2(name):
   return name[0] == 'D' or name[0] == 'N'

print is_friend('Diane')
#>>> True

print is_friend('Ned')
#>>> True

print is_friend('Moe')
#>>> False


print 'is_friend2'

print is_friend2('Diane')
#>>> True

print is_friend2('Ned')
#>>> True

print is_friend2('Moe')
#>>> False
