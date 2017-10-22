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
  <img width="400" height="400" src="https://github.com/m-gaucher/ACC_Dev/blob/master/img/">
</p>
## In Class Program 14
### Introduction
In this program, we will use a Text editor to formally write our program. The final solution MUST run successfully as a Python program. This program will demonstrate what we have learned from Chapter 5. We intend to demonstrate competencies in the following topics:

* **Non-valued Return functions**
```python
def display():
  print("Hello World!")
```

### Procedure
1. Define a display function
2. Call the display function

> :page_facing_up: [Inc12prog.py](https://github.com/m-gaucher/ACC_Dev/blob/master/CSC-119/docs/In-Class%20Program%2011%20-%2012/Inc12prog.py)
```python
'''
display_prompt: non-value return function with no parameters
'''
def display_prompt():
    print("Entering: ", display_prompt.__name__ + '()')
    print("Welcome to the display_prompt function!")

'''
main: main function of program
'''
def main():
    print("Program starting from: ", main.__name__ + '()')
    display_prompt()
    print("After function call, back to : ", main.__name__ + '()')

if __name__ == "__main__":
    main()
```
> :computer: Output
```
Program starting from:  main()
Entering:  display_prompt()
Welcome to the display_prompt function!
After function call, back to :  main()
```

