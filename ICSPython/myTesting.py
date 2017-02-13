# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay1(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def restDaysMonth(year1, month1, day1, year2, month2, day2):
   return (30 - day1) + (30 - day2)

        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
   
   if year1 == year2:
      totalRestDays = restDaysMonth(year1, month1, day1, year2, month2, day2)
      print totalRestDays
      totalDays = 0
      while month1 < month2:
         totalDays += 30
         month1 += 1
      return totalDays - totalRestDays

print daysBetweenDates(2012,9,30,2012,11,25)

#nextYear, nexMonth, nextDay = nextDay(2012,9,30)
#print nextYear, nexMonth, nextDay

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
#
#test()
    

