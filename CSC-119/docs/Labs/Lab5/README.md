# Lab 5
_Prepared for: CSC-119 Students_ /
_Prepared by: Marshall Gaucher_


**Due: Date at 11:59 PM MT**

## Part 1
### STQ From Textbook
STQ = Self-Test Questions

> :blue_book: Section 5.1.3: Questions 1, 2, 3, 5, 6, 7
> :blue_book: Section 5.2.7: Questions 1, 2, 4, 5, 6, 7, 8

* **Valued-Return Functions**
```python
def sum_two_nums(n1,n2):
  return n1+n2
```
* **Local Variable Scope**
```python
def func_scope():
  #local variable of func_scope()
  local_var1 = 0
  print(local_var1)
```
Our goal is to define a function, call a function, and ensure the return value is correct.

### Procedure
1. Define an average function that takes 3 parameters
2. Call this function with 3 parameters
3. Print the return value of this function

> :page_facing_up: [Inc11prog.py](https://github.com/m-gaucher/ACC_Dev/blob/master/CSC-119/docs/In-Class%20Program%2011%20-%2012/Inc11prog.py)
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
## In Class Program 12
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

