# Modify the get_next_target procedure so that
# if there is a link it behaves as before, but
# if there is no link tag in the input string,
# it returns None, 0.

# Note that None is not a string and so should
# not be enclosed in quotes.

# Also note that your answer will appear in
# parentheses if you print it.

def get_next_target(page):
   start_link = page.find('<a href=')
   #Insert your code below here
   if start_link == -1:
      return None, 0
   #Your code finish here @mcardoso
   start_quote = page.find('"', start_link)
   end_quote = page.find('"', start_quote + 1)
   url = page[start_quote + 1:end_quote]
   return url, end_quote
                 
WithLink = ('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

Nolink = ('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left">"http://udacity.com">')

result, value = get_next_target(WithLink)
#result, value = get_next_target(Nolink)

#print result, 'and', value

if result is not None:
   print result
else:
   print 'Does not has link'
