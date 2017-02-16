import urllib

def read_text():
   quotes = open('/home/r2d2/Udacity/PFWPython/movie_quotes.txt')
   contentes_of_file = quotes.read()
   print contentes_of_file
   quotes.close()
   check_profanity(contentes_of_file)

def check_profanity(text_to_check):
   connection = urllib.urlopen('http://www.wdylike.appspot.com/?q=shot'+text_to_check)
   output = connection.read()
   print output
   connection.close()
   if 'false' in output:
      print 'There is no profanity word'
   elif 'true' in output:
      print 'On this document has a profanity word, please a look at this!'
   else:
      print 'Here has an exception, we could not read your file, please check the path on this python script'
      


read_text()
