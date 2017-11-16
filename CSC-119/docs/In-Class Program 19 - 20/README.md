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
# declare dict
dict = {'Name ': 'Sarah ', 'Age ': 7, 'Class ': 'CSC -119 '}

# print elements by key value
print (" dict [' Name ']: ", dict ['Name '])
print (" dict ['Age ']: ", dict ['Age '])
print (" dict [' Class ']: ", dict ['Class '])

# print entire dict
print ( dict )

# update item in dict
dict ['Name ']= " Frank "
dict ['Age '] = 2
dict ['Class '] = "CSC -999 "

print ("\nUpdating record in dict :\n")
print (" dict [' Name ']: ", dict ['Name '])
print (" dict ['Age ']: ", dict ['Age '])
print (" dict [' Class ']: ", dict ['Class '])

#add item to dict
dict ['School ']= "ACC "

print ("\nAfter adding a key/ value to dict : \n")
print ( dict )

# delete item from dict
print ("\nRemoving 'NAME ' key/ value from dict : \n")
del dict ['Name ']
print ( dict )

# remove all items in a dict
print ("\nRemoving all key/ value pairs from dict : \n")
dict . clear ()
print ( dict )

# delete dict
print ("\nDeleting dict : \n")
del dict

try :
  print ( dict )
except NameError :
  print ("The dict is no longer defined .")
  print (" Without this exception you would see the following :\n")
  print ("\tTraceback ( most recent call last ):")
  print ("\tFile 'python ', line 43, in <module >")
  print ("\tNameError : name 'dict ' is not defined ")

# create 2 new dictionaries to demonstrate built -in function
dict1 = {'Name ': 'Sarah ', 'Age ': 7, 'Class ': 'CSC -119 '}
dict2 = {'Name ': 'Frank ', 'Age ': 2, 'Class ': 'CSC -999 ', 'School ': 'ACC '}

# print length of dictionaries
print ("\nLength of dictionaries : \n")
print (" dict1 : ", len( dict1 ))
print (" dict2 : ", len( dict2 ))

# print dictionaries as strings
print ("\nDictionaries as strings : \n")
print (" dict1 : ", str( dict1 ))
print (" dict2 : ", str( dict2 ))

# print dict type
print ("\nDictionary type : \n")
print (" dict1 : ", type ( dict1 ))
print (" dict2 : ", type ( dict2 ))

# print dict keys and values
print ("\nDictionary key/ value : \n")
print (" dict1 keys : ", dict1 . keys ())
print (" dict1 values : ", dict1 . values ())
print (" dict2 keys : ", dict2 . keys ())
print (" dict2 values : ", dict2 . values ())

# determine if a dict has a given key
print ("\nCheck Dictionary for a key: \n")
print (" dict1 has key 'Name ' : ", 'Name ' in dict1 )
print (" dict1 has key 'Bird ' : ", 'Bird ' in dict1 )

# create a dictionary with mutable key
temp = {( 'Jan ', 2, 2004) : 34.6 ,
        ('Jan ', 3, 2006) : 94.6 ,
        ('Jan ', 4, 2001) : 74.6}

print ("\nNew dictionary temp with mutable key :\n")
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

