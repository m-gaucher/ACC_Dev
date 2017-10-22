
# In Class Programs 9 & 10
_Prepared for: CSC-119 Students_ /
_Prepared by: Marshall Gaucher_

**Due: Date at 11:59 PM MT**

## In Class 9 
### Introduction
In this program, we will use a Text editor to formally write our program. The final solution MUST run successfully as a Python program.  This program will demonstrate what we have learned from Chapter 4.  We intend to demonstrate competencies in the following topics:

* **Lists**
```python
num_list = [0,1,2,3,4,5]
```
* **For Loops**
```python
word = "bird"
for letter in word:
  print(letter)
```
* **Range function**
```python
for num in range(6):
    print(num)
```
* **List Operations**
```python
#delcare empty list
item_list = []

#add item(s) to list
item_list.append(1)
item_list.append("Me")

#update item(s) in list
item_list[0] = 111
item_list[1] = "MeToo"

#delete entire list
del item_list
```

Our goal is to iterate forward and backward in a list.  This is to get us familiar with the basic floow of underlying functions  provided by lists.  We will then use some of these list operations to manipulate our given list.

### Procedure
1. Declare/Create a list of numbers
2. Iterate forward through the list
3. Iterate backwards through the list
4. Append an item into the list
5. Retrieve a value in a list
6. Update a value in a list
7. Insert a value in a list
8. Remove a value in a list
9. Delete a list

> Inc9prog.py
```python
#create a list
num_list = []

#appending  ints  into a list/print  forwards
for  num in  range (0,10):
    num_list.append(num+1)
    print("Appending  value:", num+1, "in index:", num)
    print("num_list  has", len(num_list), "items")
    
#iterate  backwards  through a list
for  num in  range(9,-1,-1):
    print("Index: ", num , "has  value: ", num_list[num])
    print("num_list  has", len(num_list), "items")
    
#retrieve a value  in a list
print("retrieve a value  in the  list: " , num_list [5] , "inindex 5")

#update a value  in a list
print("update a value  in a list: before ", num_list [0], end=", after ")
num_list [0]  = 9999
print(num_list [0])

#insert a value  in a list
num_list.insert(0, 44)
print("After  insert , index 0 now  contains  the  value: ", num_list [0]) 

#removing  value  in list
print("Removing  9999  from  num_list ...")
num_list.remove (9999)  
print("Now  num_list  contains: ",num_list)

#delete  the  list
num_list.clear ()
```
```output```
```sh
Appending  value: 1 in index: 0
num_list  has 1 items
Appending  value: 2 in index: 1
num_list  has 2 items
Appending  value: 3 in index: 2
num_list  has 3 items
Appending  value: 4 in index: 3
num_list  has 4 items
Appending  value: 5 in index: 4
num_list  has 5 items
Appending  value: 6 in index: 5
num_list  has 6 items
Appending  value: 7 in index: 6
num_list  has 7 items
Appending  value: 8 in index: 7
num_list  has 8 items
Appending  value: 9 in index: 8
num_list  has 9 items
Appending  value: 10 in index: 9
num_list  has 10 items
Index:  9 has  value:  10
num_list  has 10 items
Index:  8 has  value:  9
num_list  has 10 items
Index:  7 has  value:  8
num_list  has 10 items
Index:  6 has  value:  7
num_list  has 10 items
Index:  5 has  value:  6
num_list  has 10 items
Index:  4 has  value:  5
num_list  has 10 items
Index:  3 has  value:  4
num_list  has 10 items
Index:  2 has  value:  3
num_list  has 10 items
Index:  1 has  value:  2
num_list  has 10 items
Index:  0 has  value:  1
num_list  has 10 items
retrieve a value  in the  list:  6 inindex 5
update a value  in a list: before  1, after 9999
After  insert , index 0 now  contains  the  value:  44
Removing  9999  from  num_list ...
Now  num_list  contains:  [44, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
