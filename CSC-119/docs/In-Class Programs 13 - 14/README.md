# In Class Programs 13 & 14
_Prepared for: CSC-119 Students_ /
_Prepared by: Marshall Gaucher_

**Due: Date at 11:59 PM MT**

## In Class Program 13 
### Introduction
In this program, we will use a Text editor to formally write our program.
The final solution MUST run successfully as a Python program. This program will demonstrate what we have learned from Chapter 6. We intend to demonstrate competencies in the following topics:


* **Objects**
* **Importing Modules**
* **Turtle Graphics**

Our goal is to ensure our Turtle Graphics environment is stable and functioning. This will allow us to begin work on Program 1. Additionally, we intend to understand the absolute position system of the Turtle, inside the graphics window.

> :turtle: **_Before continuing please install Turtle from [here](http://pythonturtle.org/)_** 

### Procedure
1. Setup a Turtle window with a given size
2. Get a reference to the turtle window
3. Get a reference to the turtle object
4. Set the location of the turtle object

> :page_facing_up: [Inc13prog.py](https://github.com/m-gaucher/ACC_Dev/blob/master/CSC-119/docs/In-Class%20Programs%2013%20-%2014/Inc13prog.py)
```python
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
```
> :computer: Output

<p align ="left">
  <img width="400" height="400" src="https://github.com/m-gaucher/ACC_Dev/blob/master/CSC-119/docs/In-Class%20Programs%2013%20-%2014/imgs/inc13prog_screen.PNG">
</p>

## In Class Program 14
### Introduction
In this program, we will use a Text editor to formally write our program. The final solution MUST run successfully as a Python program. This program will demonstrate what we have learned from Chapter 6. We intend to demonstrate competencies in the following topics:

* **Objects**
* **Importing Modules**
* **Turtle Graphics**
* **Method Binding**
* **Event Handling**

### Procedure
1. Setup a Turtle window with a given size
2. Get a reference to the turtle window
3. Get a reference to the turtle object
4. Set the location of the turtle object
5. Bind keyboard arrow keys to given functions
6. Setup event handler to capture keyboard keys pressed by user
7. Move the Turtle based on users keyboard input

> :page_facing_up: [Inc14prog.py](https://github.com/m-gaucher/ACC_Dev/blob/master/CSC-119/docs/In-Class%20Programs%2013%20-%2014/Inc14prog.py)
```python
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
```

> :computer: Output

<p align ="left">
  <img width="400" height="400" src="https://github.com/m-gaucher/ACC_Dev/blob/master/CSC-119/docs/In-Class%20Programs%2013%20-%2014/imgs/inc14prog_screen.PNG">
</p>

'''
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
forward key pressed 
left key pressed 
right key pressed 
backward key pressed 
```



