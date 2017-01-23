# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.

def find_second(string, whatFind):
    find_first = string.find(whatFind)
    return string.find(whatFind, find_first + 1)



#danton = "De l'audace, encore de l'audace, toujours de l'audace"
#find_first = danton.find('audace')
#print find_first

#find_second = danton.find('audace', find_first + 1)
#print find_second

#print find_second(danton, 'audace')
#>>> 25

twister = "she sells seashells by the seashore"
print find_second(twister,'she')
#>>> 13
