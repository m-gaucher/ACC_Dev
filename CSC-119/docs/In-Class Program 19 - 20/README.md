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

dict_student [' Name ']:  Sarah 
 dict_student ['Age ']:  7
 dict_student [' Class ']:  CSC -119 
{'Name ': 'Sarah ', 'Age ': 7, 'Class ': 'CSC -119 '} 

key: Name  associated with value: Sarah 
key: Age  associated with value: 7
key: Class  associated with value: CSC -119 

Updating record in dict_student :

 dict_student [' Name ']:   Frank 
 dict_student ['Age ']:  2
 dict_student [' Class ']:  CSC -999 

After adding a key/ value to dict_student : 

{'Name ': ' Frank ', 'Age ': 2, 'Class ': 'CSC -999 ', 'School ': 'ACC '}

Removing 'NAME ' key/ value from dict_student : 

{'Age ': 2, 'Class ': 'CSC -999 ', 'School ': 'ACC '}

Removing all key/ value pairs from dict_student : 

{}

Deleting dict_student : 

The dict_student is no longer defined .
 Without this exception you would see the following :

	Traceback ( most recent call last ):
	File 'python ', line 43, in <module >
	NameError : name 'dict_student ' is not defined 

Length of dict_studentionaries : 

 dict_student1 :  3
 dict_student2 :  4

dict_studentionaries as strings : 

 dict_student1 :  {'Name ': 'Sarah ', 'Age ': 7, 'Class ': 'CSC -119 '}
 dict_student2 :  {'Name ': 'Frank ', 'Age ': 2, 'Class ': 'CSC -999 ', 'School ': 'ACC '}

dict_studentionary type : 

 dict_student1 :  <class 'dict'>
 dict_student2 :  <class 'dict'>

dict_studentionary key/ value : 

 dict_student1 keys :  dict_keys(['Name ', 'Age ', 'Class '])
 dict_student1 values :  dict_values(['Sarah ', 7, 'CSC -119 '])
 dict_student2 keys :  dict_keys(['Name ', 'Age ', 'Class ', 'School '])
 dict_student2 values :  dict_values(['Frank ', 2, 'CSC -999 ', 'ACC '])

Check dict_studentionary for a key: 

 dict_student1 has key 'Name ' :  True
 dict_student1 has key 'Bird ' :  False

New dict_studentionary temp with mutable key :

 temp :  {('Jan ', 2, 2004): 34.6, ('Jan ', 3, 2006): 94.6, ('Jan ', 4, 2001): 74.6}
 temp keys :  dict_keys([('Jan ', 2, 2004), ('Jan ', 3, 2006), ('Jan ', 4, 2001)])
 temp values :  dict_values([34.6, 94.6, 74.6])
 temp [(' Jan ', 2, 2004) ] : 34.6
 temp [(' Jan ', 3, 2006) ] : 94.6
 temp [(' Jan ', 4, 2001) ] : 74.6

```

## In Class Program 20
### Introduction
In this program, we will use a Text editor to formally write our program.
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
print ("\nSet Membership : \n")
print (" Value 1 in set_a : ", 1 in set_a )
print (" Value 99 in set_a : ", 99 in set_a )
print (" Value 5 in set_b : ", 5 in set_b )
print (" Value -3 in set_b : ", -3 in set_b )

#add item to list
print ("\nAdd item to Set: \n")
print (" set_a before :", set_a )
set_a.add (4)
print (" set_a after :", set_a )

# remove item to list
print ("\nAdd item to Set: \n")
print (" set_a before :", set_a )
set_a.remove (4)
print (" set_a after :", set_a )

# union
#set of elements in either set_a or set_b
print ("\nUnion : \n")
print (" union of set_a and set_b :", set_a | set_b )
print (" union of set_b and set_a :", set_b | set_a )

# intersection
# set of elements in both set_a and set_b
print ("\nIntersection : \n")
print (" intersection of set_a and set_b :", set_a & set_b )
print (" intersection of set_b and set_a :", set_b & set_a )

#difference
#set of elements in set_a , but not in set_b
print ("\nDifference : \n")
print (" difference of set_a and set_b :", set_a - set_b )
print (" difference of set_b and set_a :", set_b - set_a )

#symetric difference
#set of elements in set_a and set_b , but not both
print ("\nSymetric Difference : \n")
print ("sym difference of set_a and set_b :", set_a ^ set_b )
print ("sym difference of set_b and set_a :", set_b ^ set_a )

# size of set
print ("\nSize of set: \n")
print (" set_a size :", len( set_a ))
print (" set_b size :", len( set_b ))
```

> :computer: Output in data_out.txt

```
Print Sets :

 set_a : {1, 2, 3}
 set_b : {3, 4, 5, 6}

Set Membership : 

 Value 1 in set_a :  True
 Value 99 in set_a :  False
 Value 5 in set_b :  True
 Value -3 in set_b :  False

Add item to Set: 

 set_a before : {1, 2, 3}
 set_a after : {1, 2, 3, 4}

Add item to Set: 

 set_a before : {1, 2, 3, 4}
 set_a after : {1, 2, 3}

Union : 

 union of set_a and set_b : {1, 2, 3, 4, 5, 6}
 union of set_b and set_a : {1, 2, 3, 4, 5, 6}

Intersection : 

 intersection of set_a and set_b : {3}
 intersection of set_b and set_a : {3}

Difference : 

 difference of set_a and set_b : {1, 2}
 difference of set_b and set_a : {4, 5, 6}

Symetric Difference : 

sym difference of set_a and set_b : {1, 2, 4, 5, 6}
sym difference of set_b and set_a : {1, 2, 4, 5, 6}

Size of set: 

 set_a size : 3
 set_b size : 4
```

