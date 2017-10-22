# In Class Programs 11 & 12
_Prepared for: CSC-119 Students_ /
_Prepared by: Marshall Gaucher_

**Due: Date at 11:59 PM MT**

## In Class Program 11 
### Introduction
In this program, we will use a Text editor to formally write our program. The final solution MUST run successfully as a Python program. This program will demonstrate what we have learned from Chapter 5. We intend to demonstrate competencies in the following topics:


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

> :page_facing_up: [Inc11prog.py](www.google.com)
```python
'''
value-return function with 3 parameters n1, n2 ,n3 passed in
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
## In Class Program 10
### Introduction
In this program, we will use a Text editor to formally write our program.  The final solution MUST run successfully as a Python program.  This program will demonstrate what we have learned from Chapter 4.  We intend to demonstrate competencies in the following topics:

* **Tuples**
```python
num_tuple (0,1,2,3,4)
```
* **Tuple Operations**
```python
num_tuple (0,1,2,3,4)
max(num_tuple)
min(num_tuple)
```
* **List of Strings**
```python
string_list = ['chicken ','cow ','bird ','dog ','elk ']
```
* **List Operations**
```python
word_list = ['word1','word2','word3']
print(len(word_list))
print(word_list.count('word1'))
```
Our goal is to demonstrate the implementations and operations of Tuples. We will then revisit lists, with a list of strings.

### Procedure
1. Declare/Create a Tuple
2. Iterate a Tuple
3. Tuple Operations
4. Declare/Create a list of Strings
5. Operations on list of Strings
6. Delete a list

> :page_facing_up: [Inc10prog.py](https://github.com/m-gaucher/ACC_Dev/blob/master/CSC-119/docs/In-Class%20Program%209%20-%2010/Inc10prog.py)
```python
# create / declare a tuple
num_tuple = ()
print (" num_tuple contains : ", num_tuple )
print (" length of num_tuple : ", len( num_tuple ))

# declaring a tuple with ints
num_tuple = (1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10)
print (" Creating a tuple of ints :", num_tuple )
print (" length of num_tuple : ", len( num_tuple ))

# iterating forwards in a tuple
for num in num_tuple :
    print (" Value : ",num)
    print (" length of num_tuple : ", len( num_tuple ))

# print max value in tuple
print ("max value in tuple is: ", max( num_tuple ))

# print min value in tuple
print ("min value in tuple is: ", min( num_tuple ))

# convert tuple to list
print (" num_tuple to list : ", list ( num_tuple ))

# declare a list of strings
string_list = ['chicken ','cow ','bird ','dog ','elk ']
print (" string_list contains : ", string_list )
print (" number of values in string_list : ", len( string_list ))
```
> :computer: Output
```
num_tuple contains :  ()
length of num_tuple :  0
Creating a tuple of ints : (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
length of num_tuple :  10
Value :  1
length of num_tuple :  10
Value :  2
length of num_tuple :  10
Value :  3
length of num_tuple :  10
Value :  4
length of num_tuple :  10
Value :  5
length of num_tuple :  10
Value :  6
length of num_tuple :  10
Value :  7
length of num_tuple :  10
Value :  8
length of num_tuple :  10
Value :  9
length of num_tuple :  10
Value :  10
length of num_tuple :  10
max value in tuple is:  10
min value in tuple is:  1
num_tuple to list :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
string_list contains :  ['chicken ', 'cow ', 'bird ', 'dog ', 'elk ']
number of values in string_list :  5
```
