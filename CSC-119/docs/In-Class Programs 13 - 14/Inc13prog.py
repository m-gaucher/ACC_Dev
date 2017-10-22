#Inc13prog.py
import turtle

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
    
    #get a Turtle object
    the_turtle = turtle.getturtle()

    #change the default turtle shape
    the_turtle.shape("turtle")
    
    #set the turtle's posistion
    the_turtle.setpos(0,0)
    
if __name__ == "__main__":
    main()
