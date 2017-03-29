# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# days_count_month(2012,9,1,2012,9,4)

def days_count_month(year1, month1, day1, year2, month2, day2):
   if year1 != year2:
      total_month1 = 0
      while year1 < year2:
         while month1 < 12:
            total_month1 = total_month1 + 1
            month1 = month1 + 1
         year1 = year1 + 1
      return ((month2 - 1) + (total_month1 - 1)) * 30 + days_count(year1, month1, day1, year2, month2, day2)

   else:
      print "Veio por aqui"
      return abs((month2 - month1) * 30 - days_count(year1, month1, day1, year2, month2, day2))
      

def days_count(year1, month1, day1, year2, month2, day2):
   if month1 == month2:
      return abs(day2 - day1)

   else:
      if day1 > 1:
         total_days1 = 30 - day1
         if day2 > 1:
            total_days2 = 30 - day2
            return total_days2 + total_days1
         else:
            total_days2 = 31 - day2
            return total_days2 + total_days1
      else:
         total_days1 = 31 - day1
         if day2 > 1:
            total_days2 = 30 - day2
            return total_days2 + total_days1
         else:
            total_days2 = 31 - day2
            return total_days2 + total_days1
      

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
#def daysBetweenDates(year1, month1, day1, year2, month2, day2):
#   year, month, day = nextDay(year, month, day)


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
#
#test()
    
print str(days_count_month(2012,9,30,2012,10,30)) + " Shall be: 30"
print str(days_count_month(2012,1,1,2013,1,1)) + " Shall be: 360"
print str(days_count_month(2012,9,1,2012,9,4)) + " Shall be: 3"
#print days_count(2012,1,1,2013,1,1)
