

def total_day_remaind_year2(year1, month1, day1, year2, month2, day2):
   totalDays = 30 - day2
   totalDaysMonth = month2 * 30
   return totalDaysMonth - totalDays




def total_day_count(year1, month1, day1, year2, month2, day2):
   
# This will count the total days starting te first year and month, so right now we should count the days when year2/month2 stoped
   total = 0
   while year1 < year2:
      while month1 < 13:
         total += 30
         month1 += 1
      month1 = 1
      year1 += 1
   return total - total_day_remaind_year2(year1, month1, day1, year2, month2, day2)












print total_day_count(2012,1,1,2013,1,1)
print total_day_remaind_year2(2012,1,1,2013,1,1)
