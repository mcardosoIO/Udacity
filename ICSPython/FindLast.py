# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(string, target):
   lastPosition = -1
   while True:
      position = string.find(target, lastPosition + 1)
      print 'Last Position: ', lastPosition
      print 'Actual Position: ', position
      if position == -1:
         return lastPosition
      lastPosition = position
   return position

#start = string.find(qtd)
#print 'start at: ', start

#next = string.find(qtd, start + 1)
#print 'next at: ', next


print find_last('aaaa', 'a')
#>>> 3

#print find_last('aaaaa', 'aa')
#>>> 3

#print find_last('aaaa', 'b')
#>>> -1

#print find_last("111111111", "1")
#>>> 8

#print find_last("222222222", "")
#>>> 9

#print find_last("", "3")
#>>> -1

#print find_last("", "")
#>>> 0





