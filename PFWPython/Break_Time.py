import time
import webbrowser

def break_time(total):
   print "Here is when this program started: " + time.ctime()
   while total <= 3:
      time.sleep(5)
      webbrowser.open("https://youtu.be/V4UfAL9f74I")
      total += 1


def break_time_new_tab(total):
   print "Here is when this program started: " + time.ctime()
   while total <= 3:
      print "You shall not pass: ", total 
      time.sleep(5)
      webbrowser.open_new_tab("https://youtu.be/V4UfAL9f74I")
      total += 1
      print total
   print "Here is when this program finished: " + time.ctime()


#break_time(1)
break_time_new_tab(1)



