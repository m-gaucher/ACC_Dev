# In Class Programs 19 & 20
_Prepared for: CSC-119 Students_ /
_Prepared by: Marshall Gaucher_

**Due: 11/16/17 at 11:59 PM MT**

## In Class Program 19 
### Introduction
In this program, we will use a Text editor to formally write our program. The final solution MUST run successfully as a Python program. This program will demonstrate what we have learned from Chapter 9. We intend to demonstrate competencies in the following topics:

* **Dictionary declaration**
* **Dictionary access**
* **Alternative dictionary keys of mutable type**

Our goal is to understand the fundamental concepts of the dictionary data
structure. Additionally, we hope to contrast the difference between indexed
(e.g. list, tuples, string) and associative data structures.

### Procedure
1. Declare/Create a dictionary of values
2. Print elements by key value
3. Print entire dictionary
4. Update item in dictionary
5. Add item to dictionary
6. Delete item from dictionary
7. Remove all items in a dictionary
8. Delete dictionary
9. Print length of dictionaries
10. Print dictionaries as strings
11. Print dictionary by keys and values
12. Determine if a dictionary has a given key

> :page_facing_up: [Inc19Prog.py](https://github.com/m-gaucher/ACC_Dev/blob/master/CSC-119/docs/In-Class%20Programs%2017%20-%2018/IncProg17.py)
```python
# declare dict_student
dict_student = {'Name ': 'Sarah ', 'Age ': 7, 'Class ': 'CSC -119 '}

# print elements by key value
print (" dict_student [' Name ']: ", dict_student ['Name '])
print (" dict_student ['Age ']: ", dict_student ['Age '])
print (" dict_student [' Class ']: ", dict_student ['Class '])

# print entire dict_student
print ( dict_student, "\n" )

# print using for loop
for key,value in dict_student.items():
    print("key:", key, 'associated with value:', value)


# update item in dict_student
dict_student ['Name ']= " Frank "
dict_student ['Age '] = 2
dict_student ['Class '] = "CSC -999 "

print ("\nUpdating record in dict_student :\n")
print (" dict_student [' Name ']: ", dict_student ['Name '])
print (" dict_student ['Age ']: ", dict_student ['Age '])
print (" dict_student [' Class ']: ", dict_student ['Class '])

#add item to dict_student
dict_student ['School ']= "ACC "

print ("\nAfter adding a key/ value to dict_student : \n")
print ( dict_student )

# delete item from dict_student
print ("\nRemoving 'NAME ' key/ value from dict_student : \n")
del dict_student ['Name ']
print ( dict_student )

# remove all items in a dict_student
print ("\nRemoving all key/ value pairs from dict_student : \n")
dict_student . clear ()
print ( dict_student )

# delete dict_student
print ("\nDeleting dict_student : \n")
del dict_student

try :
  print ( dict_student )
except NameError :
  print ("The dict_student is no longer defined .")
  print (" Without this exception you would see the following :\n")
  print ("\tTraceback ( most recent call last ):")
  print ("\tFile 'python ', line 43, in <module >")
  print ("\tNameError : name 'dict_student ' is not defined ")

# create 2 new dict_studentionaries to demonstrate built -in function
dict_student1 = {'Name ': 'Sarah ', 'Age ': 7, 'Class ': 'CSC -119 '}
dict_student2 = {'Name ': 'Frank ', 'Age ': 2, 'Class ': 'CSC -999 ', 'School ': 'ACC '}

# print length of dict_studentionaries
print ("\nLength of dict_studentionaries : \n")
print (" dict_student1 : ", len( dict_student1 ))
print (" dict_student2 : ", len( dict_student2 ))

# print dict_studentionaries as strings
print ("\ndict_studentionaries as strings : \n")
print (" dict_student1 : ", str( dict_student1 ))
print (" dict_student2 : ", str( dict_student2 ))

# print dict_student type
print ("\ndict_studentionary type : \n")
print (" dict_student1 : ", type ( dict_student1 ))
print (" dict_student2 : ", type ( dict_student2 ))

# print dict_student keys and values
print ("\ndict_studentionary key/ value : \n")
print (" dict_student1 keys : ", dict_student1 . keys ())
print (" dict_student1 values : ", dict_student1 . values ())
print (" dict_student2 keys : ", dict_student2 . keys ())
print (" dict_student2 values : ", dict_student2 . values ())

# determine if a dict_student has a given key
print ("\nCheck dict_studentionary for a key: \n")
print (" dict_student1 has key 'Name ' : ", 'Name ' in dict_student1 )
print (" dict_student1 has key 'Bird ' : ", 'Bird ' in dict_student1 )

# create a dict_studentionary with mutable key
temp = {( 'Jan ', 2, 2004) : 34.6 ,
        ('Jan ', 3, 2006) : 94.6 ,
        ('Jan ', 4, 2001) : 74.6}

print ("\nNew dict_studentionary temp with mutable key :\n")
print (" temp : ", temp )
print (" temp keys : ", temp . keys ())
print (" temp values : ", temp . values ())

print (" temp [(' Jan ', 2, 2004) ] :" , temp [( 'Jan ', 2, 2004) ])
print (" temp [(' Jan ', 3, 2006) ] :" , temp [( 'Jan ', 3, 2006) ])
print (" temp [(' Jan ', 4, 2001) ] :" , temp [( 'Jan ', 4, 2001) ])

```
> :computer: Output

```

Add output from inc19

```

## In Class Program 20
### Introduction
InIn this program, we will use a Text editor to formally write our program.
The final solution MUST run successfully as a Python program. This program will demonstrate what we have learned from Chapter 9. We intend to demonstrate competencies in the following topics: this program, we will use a Text editor to formally write our program. The final solution MUST run successfully as a Python program. This program will demonstrate what we have learned from Chapter 8. We intend to demonstrate competencies in the following topics:

* **Sets**
* **Set membership**
* **Set operations**

Our goal is to demonstrate the implementations and operations of Sets. This will provide a data structure for mathematical set operations.

### Procedure
1. Declare a Set
2. Set membership
3. Add item to set
4. Remove item from set
5. Union
6. Intersection
7. Difference
8. Symmetric difference
9. Size

> :page_facing_up: [Inc20Prog.py](https://github.com/m-gaucher/ACC_Dev/blob/master/CSC-119/docs/In-Class%20Programs%2017%20-%2018/IncProg18.py)

```python
# declare a set
set_a = {1 ,2 ,3}
set_b = {3 ,4 ,5 ,6}

# print entire set
print (" Print Sets :\n")
print (" set_a :", set_a )
print (" set_b :", set_b )

#set membership
print ("\ nSet Membership : \n")
print (" Value 1 in set_a : ", 1 in set_a )
print (" Value 99 in set_a : ", 99 in set_a )
print (" Value 5 in set_b : ", 5 in set_b )
print (" Value -3 in set_b : ", -3 in set_b )

#add item to list
print ("\ nAdd item to Set: \n")
print (" set_a before :", set_a )
set_a.add (4)
print (" set_a after :", set_a )

# remove item to list
print ("\ nAdd item to Set: \n")
print (" set_a before :", set_a )
set_a.remove (4)
print (" set_a after :", set_a )

# union
#set of elements in either set_a or set_b
print ("\ nUnion : \n")
print (" union of set_a and set_b :", set_a | set_b )
print (" union of set_b and set_a :", set_b | set_a )

# intersection
# set of elements in both set_a and set_b
print ("\ nIntersection : \n")
print (" intersection of set_a and set_b :", set_a & set_b )
print (" intersection of set_b and set_a :", set_b & set_a )

#difference
#set of elements in set_a , but not in set_b
print ("\ nDifference : \n")
print (" difference of set_a and set_b :", set_a - set_b )
print (" difference of set_b and set_a :", set_b - set_a )

#symetric difference
#set of elements in set_a and set_b , but not both
print ("\ nSymetric Difference : \n")
print ("sym difference of set_a and set_b :", set_a ^ set_b )
print ("sym difference of set_b and set_a :", set_b ^ set_a )

# size of set
print ("\ nSize of set: \n")
print (" set_a size :", len( set_a ))
print (" set_b size :", len( set_b ))
```

> :computer: Output in data_out.txt

```
add output from inc20
```

