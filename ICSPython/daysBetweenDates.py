# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
#
# day = [30,30,30,30,30,30,30,30,30,30,30,30]
# month = [1,2,3,4,5,6,7,8,9,10,11,12] 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def restDaysMonth1(year1, month1, day1, year2, month2, day2):
   return day1 -30

def restDaysMonth2(year1, month1, day1, year2, month2, day2):
   return day2 -30

def totalDaysYear2(year1, month1, day1, year2, month2, day2):
   month1 = 1
   total3 = 0   
   while month1 < month2:
      total3 += 30
      month1 += 1
   return total3 - restDaysMonth2(year1, month1, day1, year2, month2, day2)

def totalDaysFirstYear1(year1, month1, day1, year2, month2, day2):   
   year1, month1, day1 = nextDay(year1, month1, day1)
   print year1, month1, day1

   total2 = 0
   month1 = 1
   while month1 < 12:
      total2 +=30
      month1 +1
      year1 += 1
   return total2    
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):

   if year1 != year2:
      total1 = 0
      while month1 < month2:
         total1 += 30
         month1 += 1
      year1 += 1
      return total1
   
   total2 = 0
   while year1 != year2:
      month1 = 1
      while month1 < 12:
         total2 +=30
         month1 +1
         year1 += 1

   return total1 + total2 - totalDaysYear2(year1, month1, day1, year2, month2, day2)




#print daysBetweenDates(2012,9,30,2012,10,30)
#print daysBetweenDates(2012,1,1,2013,10,1)
#print daysBetweenDates(2012,9,30,2012,10,30)
print totalDaysFirstYear1(2012,9,30,2012,10,30)


#    """Returns the number of days between year1/month1/day1
#       and year2/month2/day2. Assumes inputs are valid dates
#       in Gregorian calendar, and the first date is not after
#       the second."""
        
    # YOUR CODE HERE!
#    return
#def test():
#    test_cases = [((2012,9,30,2012,10,30),30), 
#                  ((2012,1,1,2013,1,1),360),
#                  ((2012,9,1,2012,9,4),3)]
#    
#    for (args, answer) in test_cases:
#        result = daysBetweenDates(*args)
#        if result != answer:
#            print "Test with data:", args, "failed"
#        else:
#            print "Test case passed!"

#test()
    

