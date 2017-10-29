# In Class Programs 15 & 16
_Prepared for: CSC-119 Students_ /
_Prepared by: Marshall Gaucher_

**Due: Date at 11:59 PM MT**

## In Class Program 15 
### Introduction
In this program, we will use a Text editor to formally write our program. The final solution MUST run
successfully as a Python program. This program will demonstrate what we have learned from Chapter 7.
We intend to demonstrate competencies in the following topics:


* **Modules**
* **Top-down design**
* **Constants**

Our goal is to import modules and demonstrate their functionality. This will allow us to continue work
on Program 1. Additionally, we intend to demonstrate concepts of the time module to recognize
measuring a given duration of time.

> :turtle: **_Please ensure you have Turtle from [here](http://pythonturtle.org/)_** 

### Procedure
1. import math module
2. import time module
3. import calendar module
4. call functions of the math module
5. call functions of the time module
6. call functions to format time structure
7. call functions to print a given month for a given year

> :page_facing_up: [Inc15Prog.py](https://github.com/m-gaucher/ACC_Dev/blob/master/CSC-119/docs/In-Class%20Programs%2015%20-%2016/IncProg15.py)
```python
#import Python modules
import math
import time
import calendar

#common math functions
print (math.ceil(4.4))
print (math.fabs(-2))
print (math.factorial(6))
print (math.fsum([1,2,3,4]))
print (math.gcd(2,22))
print (math.pow(2,3))

#trigonometry
print (math.acos(0))
print (math.cos(0))

#math constants
print (math.pi)
print (math.e)

#print epoch time jan 1st 12:00am 1970
print ("Current EPOCH time: ", time.time())

#print process time(typically used to measure process time of function call)
print ("CPU time:", time.clock())

#local time; get time struct
ltime = time.localtime(time.time())
print ("Current local time: ", ltime)

#format time struct
fltime = time.asctime(time.localtime(time.time()))
print ("Current formatted local time: ", fltime)

#sleep the main thread for x second; .001 = 1 millisecond ; 1 = 1 second
time.sleep(2)

#calendar print a given month of a year
cmonth = calendar.month(2010, 1)
print ("Calendar month below:")
print (cmonth)
```
> :computer: Output

```

5
2.0
720
10.0
2
8.0
1.5707963267948966
1.0
3.141592653589793
2.718281828459045
Current EPOCH time:  1509297942.603461
CPU time: 0.063952
Current local time:  time.struct_time(tm_year=2017, tm_mon=10, tm_mday=29, tm_hour=17, tm_min=25, tm_sec=42, tm_wday=6, tm_yday=302, tm_isdst=0)
Current formatted local time:  Sun Oct 29 17:25:42 2017
Calendar month below:
    January 2010
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31

```

## In Class Program 16
### Introduction
In this program, we will use a Text editor to formally write our program. The final solution MUST run
successfully as a Python program. This program will demonstrate what we have learned from Chapter 7.
We intend to demonstrate competencies in the following topics:

* **Modules**
* **Creating your own module**

### Procedure
1. Define a function within a module
2. Save this file as <your_module_name>.py
3. Import this file in your python program
4. Call functions from your created module

> :page_facing_up: custom_module.py
```python
def hello_world():
    print ("Hello World!!", ":", __name__)
    
def hello_sum(x,y):
    print(x, ",", y, ":", __name__)
    return x + y
    
def hell0_diff(x,y):
    print(x, ",", y, ":", __name__)
    return x - y

def main():
    print("Entering main():", ":", __name__)

if __name__ == "__main__":
    main()
else:
    print(__name__ + ".py", " is being imported...")
```
> :page_facing_up:  test_prog_module.py
```python

#import created module; ensure it is atleast within the same directory as custom_module.py
import custom_module

#call functions of the above module
custom_module.hello_world()
custom_module.hello_sum(2,2)
custom_module.hell0_diff(4,2)

```

> :computer: Output



```

```

> :books: Turtle Resources [here](https://docs.python.org/2/library/turtle.html#)




