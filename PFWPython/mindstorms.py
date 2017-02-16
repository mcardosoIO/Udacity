import turtle

def draw_square(some_turtle):
   for i in range(1,5):
      some_turtle.forward(100)
      #on bellow method "90" means 90 degrees to right
      some_turtle.right(90)


def draw_art():
   window = turtle.Screen()
   window.bgcolor('Blue')
   # Here I'll create an instance called supersquare
   supersquare = turtle.Turtle()
   supersquare.shape('turtle')
   supersquare.color('white')
   supersquare.speed(2)
   for i in range(1,37):
      draw_square(supersquare)
      supersquare.right(10)
      
   window.exitonclick()

draw_art()


