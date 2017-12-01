# Turtle Program

Below is the demo code from class with a few modifications.

_Note: resolved specific IDE window issue causing instant window close after window.listen()_

```python
import turtle
import time
from tkinter import messagebox

# setup the turtle object in global space
the_turtle = turtle.getturtle()

# create variables to store statistics of the turtle path
start_time = 0
end_time = 0
distance = 0

# create a "legend" for values in the map
START_LOC = 1
END_LOC = 2
OBST_LOC = 3

# create vars to width and height of map
MAP_WIDTH = 250
MAP_HEIGHT = 250
TURN_DEGREE = 90

# create the maze for underlying map logic
# (e.g. start location, obstacle location, end location)
maze = [[0] * MAP_WIDTH for i in range(MAP_HEIGHT)]

'''
mark_point_visually
'''
def mark_point_visually(point_code, x, y):
    #pick up the pen to avoid lines draw to each location
    the_turtle.penup()

    if( point_code == OBST_LOC):
        the_turtle.color("red")
    if (point_code == START_LOC):
        the_turtle.color("blue")
    if (point_code == END_LOC):
        the_turtle.color("green")

    the_turtle.shape("circle")
    the_turtle.shapesize(.1, .1, 1)
    the_turtle.setposition(x, y)
    the_turtle.pendown()
    the_turtle.stamp()
    the_turtle.penup()

    #reset turtle object state
    the_turtle.shapesize(1, 1, 1)
    the_turtle.shape("turtle")
    the_turtle.fillcolor("black")

'''
display_end_prompt: used to display end statistics to user via message box widget
'''
def display_end_prompt():
    global end_time
    end_time = time.time()
    end_location_str = "End Location Reached!!!" + \
                       "\nElapsed time: " + str((end_time - start_time)) + \
                       "\nDistance: " + str(distance)
    messagebox.showinfo("Information", end_location_str)

'''
forward: used to bind keyboard up arrow key to control turtle
'''
def forward():
    global distance

    print("forward key pressed ")
    print("x:", round(the_turtle.xcor()), "y:", round(the_turtle.ycor()))

    # start the timer on the first turtle movement
    if(distance == 0):
        global start_time
        start_time = time.time()

    # check if the turtle has reached the end location
    if (maze[round(the_turtle.xcor())][round(the_turtle.ycor())] == END_LOC):
        display_end_prompt()

    '''
    Since the coordinate system is fixed to the top left corner of the window, 
    and we assume the turtle only checks valid points looking forward, 
    ensure the location that is turtle distance ahead is open (e.g. != 3)
    '''
    if (maze[round(the_turtle.xcor())][round(the_turtle.ycor()) + 20] == OBST_LOC ):
        print("OBSTACLE: ", "x:", round(the_turtle.xcor()), "y:", round(the_turtle.ycor()+20))
    elif(maze[round(the_turtle.xcor()) + 20][round(the_turtle.ycor())] == OBST_LOC):
        print("OBSTACLE: ", "x:", round(the_turtle.xcor()+20), "y:", round(the_turtle.ycor()))
    else:
        the_turtle.forward(1)
        distance += 1

'''
backward: used to bind keyboard down arrow key to control turtle
'''
def backward():
    the_turtle.backward(1)
    print("backward key pressed ")

'''
left: used to bind keyboard left arrow key to control turtle
'''
def left():
    the_turtle.left(TURN_DEGREE)
    print("left key pressed ")

'''
right: used to bind keyboard right arrow key to control turtle
'''
def right():
    the_turtle.right(TURN_DEGREE)
    print("right key pressed ")

'''
main: main function of program
'''
def main():
    # get locations from user
    startx = int(input("Enter startx:"))
    starty = int(input("Enter starty:"))
    obsx = int(input("Enter obsx:"))
    obsy = int(input("Enter obsy:"))
    endx = int(input("Enter endx:"))
    endy = int(input("Enter endy:"))

    # mark x, y locations in maze
    maze[startx][starty] = START_LOC
    maze[endx][endy] = END_LOC
    maze[obsx][obsy] = OBST_LOC

    # set window size
    turtle.setup(MAP_WIDTH, MAP_HEIGHT)

    # get reference to turtle window
    window = turtle.Screen()

    # set window title bar
    window.title("Turtle Program v1.0.0.0")

    # bind up keyboard arrow to forward function
    window.onkey(forward, "Up")

    # bind up keyboard arrow to backward function
    window.onkey(backward, " Down ")

    # bind up keyboard arrow to right function
    window.onkey(right, " Right ")

    # bind up keyboard arrow to left function
    window.onkey(left, " Left ")

    #align the map on the top-left corner of the window
    window.setworldcoordinates(0, MAP_WIDTH, MAP_HEIGHT, 0)

    # mark the obstacle location
    mark_point_visually(OBST_LOC, obsx, obsy)

    # mark the end location
    mark_point_visually(END_LOC, endx, endy)

    #set the turtle to the starting location
    the_turtle.setposition(startx, starty)
    the_turtle.pendown()

    # setup event handler
    window.listen()

    # this line is not needed for all implementations,
    # however certain IDEs will instantly close window
    # after calling window.listen()
    turtle.mainloop()

if __name__ == "__main__":
    main()
```
