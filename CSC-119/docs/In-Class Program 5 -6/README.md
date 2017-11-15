
# In Class Programs 5 & 6
_Prepared for: CSC-119 Students_ /
_Prepared by: Marshall Gaucher_

**Due: Date at 11:59 PM MT**

## In Class Program 5 
### Introduction
In this program, we will transition into a Text editor to formally write our program. You can still use the
interpreter to sanity check your arithmetic, but the final solution MUST run successfully as a Python
program. This program will summarize what we have learned from Chapter 2. We intend to
demonstrate competencies in the following topics:

* **Expressions**
```python
x = 2 + 4
```
* **Data Types**
```python
x = 2         #type int
word = "bird" #type string
num = 2.333   #type float
```
* **Operator Precedence**
```
PEMDAS
Parantheses     ()
Exponentiation  ** 
Multiplication  * 
Division        /
Addition        +
Subtraction     -
```
* **Operator Associativity**
```
See In-Class Presentations

```
* **Coercion**
```python
x = 4
y = 2.44444
z = 0

z = x + y
```

* **Type Conversion**
```python
int(2.333333)
float(2)
str(2)
```

Our goal is to convert temperature data entered by the user. We will use the Temperature Conversion
Program as a baseline to get us started.


### Procedure
1. Print a program greeting (e.g. Generally describe what this program does)
2. Prompt the user for the temperature (this is in Fahrenheit)
3. Calculate degrees Celsius
   - Celsius = (Fahrenheit – 32) * 5 / 9
4. Calculate Kelvin
   - Kelvin = Celsius + 273.15
5. Calculate degrees Rankine
   - Rankine = Fahrenheit + 459.67
6. Output degrees Celsius
   - ```print(Fahrenheit, “F \xb0 equals “, format(Celsius, ‘.2f’’), “C \xb0”)```
7. Output Kelvin
   - ```print(Fahrenheit, “F \xb0 equals “, format(Kelvin, ‘.2f’’), “K”)```
8. Output degrees Rankine
   - ```print(Fahrenheit, “F \xb0 equals “, format(Rankine, ‘.2f’’), “R \xb0”)```

> :page_facing_up: [Inc5prog.py](https://github.com/m-gaucher/ACC_Dev/blob/master/CSC-119/docs/In-Class%20Program%209%20-%2010/Inc9prog.py)
```python
Need to add code from D2L
```
> :computer: Output
```
Add output
```
## In Class Program 6
### Introduction
In this program, we will use a Text editor to formally write our program. The final solution MUST run
successfully as a Python program. This program will demonstrate what we have learned from Chapter 3.
We intend to demonstrate competencies in the following topics:

* **Sequential control**
```python

```
* **Boolean Expressions**
```python

```
* **Membership Operators**
```python

```
* **Selection Control**
```python

```
Our goal is to convert class points, entered by a user, to a letter grade and value. We will use the class
syllabus as a baseline to get us started. As we saw in class, it is easier to use ints as bounds, but you can
use other data types too (e.g. floats).

### Procedure
1. Print a program greeting (e.g. Generally describe what this program does)
2. Prompt the user for the class points (e.g. 450)
3. If the class point is 405 or more
   - Output letter grade of A and the value of their points (e.g 450/450 = 100.00 %)
4. If the class point is between 360 and 404
   - Output letter grade of B and the value of their points (e.g 370/450 = 82.22 %)
5. If the class point is between 315 and 359
   - Output letter grade of C and the value of their points
6. If the class point is between 270 and 314
   - Output letter grade of D and the value of their points
7. If the class points is between 269 and 0
   - Output letter grade of F and the value of their points
8. If the class point is greater than 450
   - Output letter grade of A++ and the value of their points
9. If the class point is less than 0
   - Output “Invalid Input” 


> :page_facing_up: [Inc6prog.py](https://github.com/m-gaucher/ACC_Dev/blob/master/CSC-119/docs/In-Class%20Program%209%20-%2010/Inc10prog.py)
```python
Add code from D2L
```
> :computer: Output
```
Add output from code
```
