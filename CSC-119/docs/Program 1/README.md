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
mark_border: marks the square maze/map border walls with OBST_LOC value

* Note: assume square maze/map 
'''
def mark_border():
    for i in range(MAP_WIDTH-1):
       maze[i][0] = OBST_LOC
       maze[MAP_WIDTH - 1][i] = OBST_LOC
       maze[i][MAP_WIDTH - 1] = OBST_LOC
       maze[0][i] =  OBST_LOC

'''
draw_border: draws the border walls for the square maze
'''
def draw_border():
    the_turtle.setposition(0,0)
    the_turtle.shape("circle")
    the_turtle.color("black")
    the_turtle.pendown()

    the_turtle.setposition(0,0)
    # draw first bottom row
    the_turtle.forward(MAP_WIDTH)
    the_turtle.left(90)
    # draw right column
    the_turtle.forward(MAP_HEIGHT)
    the_turtle.left(90)
    # draw top row
    the_turtle.forward(MAP_WIDTH)
    the_turtle.left(90)
    # draw left column
    the_turtle.forward(MAP_HEIGHT)

    # mark the maze with border walls
    mark_border()

    the_turtle.shape("classic")
    the_turtle.color("black")
    the_turtle.penup()

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
    # use conventional integer round to avoid off by 1 issues
    x = round(the_turtle.xcor())
    y = round(the_turtle.ycor())

    print("forward key pressed ")
    print("x:", x, "y:", y)

    # start the timer on the first turtle movement
    if(distance == 0):
        global start_time
        start_time = time.time()

    # check if the turtle has reached the end location
    if (maze[x][y] == END_LOC):
        display_end_prompt()

    '''
    Since the coordinate system is fixed to the top left corner of the window, 
    and we assume the turtle only checks valid points looking forward, 
    ensure the location that is turtle distance ahead is open (e.g. != 3)
    
    ** Note: 20 pixels is the length of the turtle; if you use another icon
    you need to scale this var accordingly
    '''
    if (maze[x][y + 1] == OBST_LOC ):
        print("OBSTACLE: ", "x:", x, "y:", y+1)
        the_turtle.backward(1)
    elif(maze[x + 1][y] == OBST_LOC):
        print("OBSTACLE: ", "x:", x+1, "y:", y)
        the_turtle.backward(1)
    else:
        the_turtle.forward(1)
        distance += 1

'''
backward: used to bind keyboard down arrow key to control turtle

*Note: we don't check for maze values backing up; assume forward orientation
'''
def backward():
    the_turtle.backward(1)
    print("backward key pressed ")

'''
left: used to bind keyboard left arrow key to control turtle
'''
def left():
    the_turtle.left(TURN_DEGREE)
    #the_turtle.right(TURN_DEGREE)
    print("left key pressed ")

'''
right: used to bind keyboard right arrow key to control turtle
'''
def right():
    the_turtle.right(TURN_DEGREE)
    #the_turtle.left(TURN_DEGREE)
    print("right key pressed ")

'''
validate_x: Ensures user enters a valid x location
*Note: border will occupy 0 and MAP_WIDTH x index of maze
'''
def validate_x(point_name):
    prompt = "Enter " + point_name + ":"
    x = int(input(prompt))

    while x <= 0 or x >= MAP_WIDTH-1:
        print("Invalid x point. Please enter a valid x between 0 and", MAP_WIDTH)
        x = int(input(prompt))

    return x

'''
validate_y: Ensures user enters a valid y location
*Note: border will occupy 0 and MAP_HEIGHT y index of maze
'''
def validate_y(point_name):
    prompt = "Enter " + point_name + ":"
    y = int(input(prompt))

    while y <= 0 or y >= MAP_HEIGHT - 1:
        print("Invalid y point. Please enter a valid y between 0 and", MAP_HEIGHT)
        y = int(input(prompt))

    return y

'''
main: main function of program
'''
def main():
    # get locations from user
    startx = validate_x("startx")
    starty = validate_y("starty")
    obsx = validate_x("obsx")
    obsy = validate_y("obsy")
    endx = validate_x("endx")
    endy = validate_y("endy")

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

    #align the map on the bottom-left corner of the window
    window.setworldcoordinates(0, 0, MAP_HEIGHT, MAP_WIDTH)

    # mark the obstacle location
    mark_point_visually(OBST_LOC, obsx, obsy)

    # mark the end location
    mark_point_visually(END_LOC, endx, endy)

    draw_border()

    #set the turtle to the starting location
    the_turtle.setposition(startx, starty)
    the_turtle.pendown()

    # set window size
    turtle.setup(MAP_WIDTH + 200, MAP_HEIGHT + 200)

    # setup event handler
    window.listen()

    # this line is not needed for all implementations,
    # however certain IDEs will instantly close window
    # after calling window.listen()
    turtle.mainloop()

if __name__ == "__main__":
    main()
```
