Demo code from class

```python
import turtle
from tkinter import messagebox
import random
import time
import math

start_time = 0
end_time = 0
distance = 0
#setup the turtle object in global space
the_turtle = turtle.getturtle()

maze = [[0] * 250 for i in range(250)]

'''
forward: used to bind keyboard up arrow key to control turtle
'''
def forward():
    global distance
    distance += 1
    print("forward key pressed ")
    print("x:", round(the_turtle.xcor()), "y:", round(the_turtle.ycor()))

    if(maze[round(the_turtle.xcor())][round(the_turtle.ycor())] == 2):
        global end_time
        end_time = time.time()
        messagebox.showinfo("Information","Yippy")
        print("Elapsed time: ", end_time - start_time)
        print("distance: ", distance)

    if(maze[round(the_turtle.xcor())][round(the_turtle.ycor())+20] != 3 and
       maze[round(the_turtle.xcor())+20][round(the_turtle.ycor())] != 3):
        the_turtle.forward(1)
    else:
        print("OBSTACLE!!!")

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
    the_turtle.left(45)
    print("left key pressed ")

'''
right: used to bind keyboard right arrow key to control turtle
'''
def right():
    the_turtle.right(45)
    print("right key pressed ")


'''
main: main function of program
'''
def main():
    window_title = "My first Turtle Graphics Program"
    window_width = 250
    window_height = 250
    startx = 0
    starty = 0
    endx = 0
    endy = 0

    startx = int(input("Enter startx:"))
    starty = int(input("Enter starty:"))
    obsx = int(input("Enter obsx:"))
    obsy = int(input("Enter obsy:"))
    endx = int(input("Enter endx:"))
    endy = int(input("Enter endy:"))

    maze[startx][starty]=1
    maze[endx][endy]=2
    maze[obsx][obsy]=3
    
    #set window size
    turtle.setup(window_width,window_height)
    
    #get reference to turtle window 
    window = turtle.Screen()
    
    #set window title bar
    window.title(window_title)

    #bind up keyboard arrow to forward function
    window.onkey( forward , "Up")

    #bind up keyboard arrow to backward function
    window.onkey( backward , " Down ")

    #bind up keyboard arrow to right function
    window.onkey(right , " Right ")

    #bind up keyboard arrow to left function
    window.onkey(left , " Left ")

    window.setworldcoordinates(0,250,250,0)

    the_turtle.penup()
    the_turtle.color("red")
    the_turtle.shape("circle")
    the_turtle.shapesize(.1,.1,1)
    the_turtle.setposition(obsx,obsy)
    the_turtle.pendown()
    the_turtle.stamp()
    the_turtle.penup()
    the_turtle.shapesize(1,1,1)

    the_turtle.penup()
    the_turtle.color("blue")
    the_turtle.shape("circle")
    the_turtle.shapesize(.1,.1,1)
    the_turtle.setposition(endx,endy)
    the_turtle.pendown()
    the_turtle.stamp()
    the_turtle.penup()
    the_turtle.shapesize(1,1,1)

    the_turtle.shape("turtle")
    the_turtle.fillcolor("black")
    the_turtle.setposition(startx,starty)
    the_turtle.pendown()
    
    #change the default turtle shape
    
    global start_time
    start_time = time.time()
    #setup event handler
    window.listen()
    
if __name__ == "__main__":
    main()

```
