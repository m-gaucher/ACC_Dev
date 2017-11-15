
# In Class Programs 3 & 4
_Prepared for: CSC-119 Students_ /
_Prepared by: Marshall Gaucher_

**Due: Date at 11:59 PM MT**

## In Class Program 3 
### Introduction
In this program, we will make use of the Python 3.5.2 shell to gain knowledge
of the material we have learned from Chapter 2. Specifcally, we intend to
practice demonstrating competencies in the following topics:

* **Numeric Literals (int,float)**
```python
x = 2     #int
num = 2.0 #float
```
* **String Literals (string)**
```python
word = "bird" #type string
```
* **Use of Python's built-in functions (format(), ord(), id())**
```
format (ord('M'), '.4e')
format (id('M'), '.4e')

```
* **Use of Control Characters**
```
\t
\n
```
Our goal is to get Unicode values for a given string and format their
output accordingly. Along the way, we will learn some techniques, which we
can expand, to create our algorithm.


### Procedure
1. Print an output line to the console
2. Print an output line to the console containing Unicode values
3. Print an output line to the console containing Unicode values, with
specific formatting
4. Print Unicode values with different notations and precision
5. Print a Unicode value with appending formatting characters
6. Print the id of a literal
7. Print the id of a variable

> :page_facing_up: [Inc3prog.py]
```python
#1
print (" output ")

#2
print ("ord value of \' M \' is: ", ord ('M'))

#3
print ("ord value of \' M \' with formatting : ")
print ( format (ord('M'), '.4f'))

#4
print ("ord value of \' M \' with different notation : ")
print ( format (ord('M'), '.4e'))

#5
print ("ord value of \' M \' with different notation : ")
print ( format (ord('M'), '.2e') + '\t characters ')

#6
print ("id of numeric literal 3 is: ")
print (id(3))

print ("id of string literal \'s\' is: ")
print (id('s'))

#7
num = 4
print ("id of variable num is: ")
print (id(num ))

word = " bird "
print ("id of variable word is: ")
print (id( word ))
```

> :computer: Output
```
output 
ord value of ' M ' is:  77
ord value of ' M ' with formatting : 
77.0000
ord value of ' M ' with different notation : 
7.7000e+01
ord value of ' M ' with different notation : 
7.70e+01	 characters 
id of numeric literal 3 is: 
139624915052352
id of string literal 's' is: 
139624895725616
id of variable num is: 
139624915052384
id of variable word is: 
139624870633632
```
## In Class Program 4
### Introduction
In this program, we will take what we have learned from our practice with
the Python 3.5.2 shell, and create an algorithm. Specifically, we intend to
practice demonstrating competencies in the following topics:

* **Algorithm Development**
* **Variables and Identifiers**
* **Operators**

Again, our goal is to take the prior learned techniques and formalize them
into more of a program like structure. It is now recommended to use a text
editor, so we can simplify execution of our code.

### Procedure
1. Prompt user for input and store to a variable
2. Print the sum of Unicode values of this string
3. Print the difference of Unicode values of this string
4. Print the product of Unicode values of this string
5. Print the quotient of Unicode values of this string
6. Print the mod value of each of the Unicode values of this string
7. Print/demonstrate a combined string and int 


> :page_facing_up: [Inc4prog.py]

```python
#1
# Enter 'Ben ' to simpify example below
name = input (" Please enter your name : ")
print ("The value stored in name is: ", name )

#2
# We will assume name is Ben; we will discuss ways to itereate later
ord_sum = ord ('B') + ord('e') + ord('n')

print ("The sum of the unicode values are: ")
print (ord('B'), " + ", ord('e')," + ", ord('n'), " = ", ord_sum )

#3
# Assume name is Ben; we will discuss ways to itereate later
ord_diff = ord('B') - ord('e') - ord('n')
print ("The difference of the unicode values are: ")
print (ord('B'), " - ", ord('e')," - ", ord('n'), " = ", ord_diff )

#4
# Assume name is Ben; we will discuss ways to itereate later
ord_prod = ord('B') * ord('e') * ord('n')
print ("The product of the unicode values are: ")
print (ord('B'), " * ", ord('e')," * ", ord('n'), " = ", ord_prod )

#5
# Assume name is Ben; we will discuss ways to itereate later
ord_quot = ord('B') / ord('e') / ord('n')
print ("The quotient of the unicode values are: ")
print (ord('B'), " / ", ord('e')," / ", ord('n'), " = ", ord_quot )

#6
# Assume name is Ben; we will discuss ways to itereate later
random_val = 5
print ("The mod values of the unicodes , using 5, are: ")
print (ord('B'), " % ", random_val , " = ", ord('B') % random_val )
print (ord('e'), " % ", random_val , " = ", ord('e') % random_val )
print (ord('n'), " % ", random_val , " = ", ord('n') % random_val )

#7
num = 10
word = " bird "

print ("If we combine string \' bird \' and int 10: ")
# The below print () will produce an error
# print ( word + num)

# Traceback ( most recent call last ):
# File " python ", line 43 , in <module >
# TypeError : must be str , not int

print ( word + str(num ))
num2 = 11
letterish = '3'
print ("If we combine string \'3\' and int 11: ")
# The below operation will produce an error
# combine = num2 + letter

# Traceback ( most recent call last ):
# File " python ", line 56 , in <module >
# TypeError : unsupported operand type (s) for +: 'int ' and 'str '

#To overcome this we must ensure the data types are of valid type
print ( num2 + int( letterish ))
```

> :computer: Output
```
Please enter your name :  John
The value stored in name is:  John
The sum of the unicode values are: 
66  +  101  +  110  =  277
The difference of the unicode values are: 
66  -  101  -  110  =  -145
The product of the unicode values are: 
66  *  101  *  110  =  733260
The quotient of the unicode values are: 
66  /  101  /  110  =  0.005940594059405941
The mod values of the unicodes , using 5, are: 
66  %  5  =  1
101  %  5  =  1
110  %  5  =  0
If we combine string ' bird ' and int 10: 
 bird 10
If we combine string '3' and int 11: 
14
```

