#Inc14prog.py
import turtle

#setup the turtle object in global space
the_turtle = turtle.getturtle()

'''
forward: used to bind keyboard up arrow key to control turtle
'''
def forward():
    the_turtle.forward(1)
    print("forward key pressed ")

'''
backward: used to bind keyboard down arrow key to control turtle
'''    
def backward():
    the_turtle.backward(1)
    print("backward key pressed ")

'''
left: used to bind keyboard left arrow key to control turtle
'''
def left ():
    print("left key pressed ")

'''
right: used to bind keyboard right arrow key to control turtle
'''
def right():
    print("right key pressed ")


'''
main: main function of program
'''
def main():
    window_title = "My first Turtle Graphics Program"
    window_width = 400
    window_height = 400
    startx = 0
    starty = 0
    
    #set window size
    turtle.setup(window_width,window_height)
    
    #get reference to turtle window 
    window = turtle.Screen()
    
    #set window title bar
    window.title(window_title)
    
    #change the default turtle shape
    the_turtle.shape("turtle")
    
    #set the turtle's posistion
    the_turtle.setpos(0,0)

    #bind up keyboard arrow to forward function
    window.onkey( forward , "Up")

    #bind up keyboard arrow to backward function
    window.onkey( backward , " Down ")

    #bind up keyboard arrow to right function
    window.onkey(right , " Right ")

    #bind up keyboard arrow to left function
    window.onkey(left , " Left ")

    #setup event handler
    window.listen()
    
if __name__ == "__main__":
    main()
