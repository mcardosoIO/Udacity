
def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def rest_day_month(year1, month1, day1, year2, month2, day2):
   return 30 - day1, 30 - day2

def first_last_year_days(year1, month1, day1, year2, month2, day2):
   if year1 != year2:
      rest1, rest2 = rest_day_month(year1, month1, day1, year2, month2, day2)
   
      year1, month1, day1 = nextDay(year1, month1, day1)
      year2, month2, day2 = nextDay(year2, month2, day2)
      
      while year1 != year2:
         total1 = 12 - month1
         year1 += 1
         if year1 != year2:


#      total1 = 12 - month1 
#      print 'Total1:', total1, 'Rest1:', rest1

#      total2 = 12 - month2
#      print 'Total2:', total2, 'Rest2:', rest2

      return (total1*30 - rest1) + (total2*30 - rest2)

   else:
      rest1, rest2 = rest_day_month(year1, month1, day1, year2, month2, day2)
   
      year1, month1, day1 = nextDay(year1, month1, day1)
      year2, month2, day2 = nextDay(year2, month2, day2)

      total3 = ((month2 - month1)*30) - (rest1 + rest2)
      return total3 


def total_day_year(year1, month1, day1, year2, month2, day2):
   return ((year2 - year1)*12)*30

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
   totalLastDays = first_last_year_days(year1, month1, day1, year2, month2, day2)
   print 'totallastdays:', totalLastDays
   todayDayYear = total_day_year(year1, month1, day1, year2, month2, day2)
   print 'toaldayeyar:', todayDayYear   

   return totalLastDays - todayDayYear



#print total_day_year(2012,6,01,2013,6,15)
#print first_last_year_days(2012,6,01,2013,6,15)
print daysBetweenDates(2012, 1, 1, 2013, 1, 1)
#print daysBetweenDates(2012,9,30,2012,10,30)
#print daysBetweenDates(2012,1,1,2013,1,1)
