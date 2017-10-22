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

``` **_Before continuing please install Turtle from [here](http://pythonturtle.org/)_** ```

### Procedure
1. Setup a Turtle window with a given size
2. Get a reference to the turtle window
3. Get a reference to the turtle object
4. Set the location of the turtle object

> :page_facing_up: [Inc13prog.py](https://github.com/m-gaucher/ACC_Dev/blob/master/CSC-119/docs/In-Class%20Program%2011%20-%2012/Inc11prog.py)
```python
'''
average: value-return function with 3 parameters n1, n2 ,n3 passed in
'''
def average(n1,n2,n3):
    print("Entering: ", average.__name__ + '()')
    return (n1+n2+n3) / 3.0

'''
main: main function of program
'''
def main():
    avg = 0.0
    print("average before function call:", avg)
    avg = average(1,2,3)
    print("average after function call:", avg)

if __name__ == "__main__":
    main()
```
> :computer: Output
```
average before function call: 0.0
Entering:  average()
average after function call: 2.0
```
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

