
class Parent():
   def __init__(self, last_name, eye_color):
      print "Parent Constructor was called"
      self.last_name = last_name
      self.eye_color = eye_color

   def show_info(self):
      print "Last Name: " + self.last_name
      print "Eye Color: " + self.eye_color

class Child(Parent):
   def __init__(self, last_name, eye_color, number_of_toys):
      print "Child Constructor was called"
      Parent.__init__(self, last_name, eye_color)
      self.number_of_toys = number_of_toys

#Below we can see a function on this subclass that has the same name of main class, this we call Method Overriding
   def show_info(self):
      print "Last Name: " + self.last_name
      print "Eye Color: " + self.eye_color
      print "Number of Toys: " + str(self.number_of_toys)


billy_cyrus = Parent("Cyrus", "blue")
billy_cyrus.show_info()

miley_cyrus = Child("Cyrus", "black", 5)
miley_cyrus.show_info()
#print miley_cyrus.last_name
#print miley_cyrus.number_of_toys
