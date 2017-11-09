# In Class Programs 17 & 18
_Prepared for: CSC-119 Students_ /
_Prepared by: Marshall Gaucher_

**Due: 11/9/17 at 11:59 PM MT**

## In Class Program 17 
### Introduction
In this program, we will use a Text editor to formally write our program. The final solution MUST run successfully as a Python program. This program will demonstrate what we have learned from Chapter 8. We intend to demonstrate competencies in the following topics:

* **Opening a file in read mode**
* **Reading data from an input file**
* **Reading data from an input file in binary mode**
* **Closing an input file**

Our goal is to demonstrate the fundamental concepts of file I/O. We intent to understand the proper mechanisms used to maintain a file handle gracefully.

### Procedure
1. Create a text file called data.txt
   - Ensure you know where this file exists
   - Use IDLE to create/save text file text file (simplifies path issues with data.txt)
2. Open the text file in read mode
3. Read and print each line of the file
4. Close the file

> :memo: data.txt
```
This is the first line in the file.
This is the second line in the file.
This is the third line in the file.
```

> :page_facing_up: [Inc17Prog.py](https://github.com/m-gaucher/ACC_Dev/blob/master/CSC-119/docs/In-Class%20Programs%2017%20-%2018/IncProg17.py)
```python
#open file in read mode 
input_file = open("data.txt", "r") 

#read each line of the file 
for line in input_file: 
  print (line) 

#close file 
input_file.close()

```
> :computer: Output

```

This is the first line in the file.
This is the second line in the file.
This is the third line in the file.

```

## In Class Program 18
### Introduction
In this program, we will use a Text editor to formally write our program. The final solution MUST run successfully as a Python program. This program will demonstrate what we have learned from Chapter 8. We intend to demonstrate competencies in the following topics:

* **Opening a file in write mode**
* **Writing data to a file**
* **Closing a output file**

Our goal is to demonstrate the fundamental concepts of file I/O. We intent to understand the proper mechanisms used to maintain a file handle gracefully.

### Procedure
1. Open a file in write mode
2. Write text to a file
3. Close the file

> :page_facing_up: [Inc18Prog.py](https://github.com/m-gaucher/ACC_Dev/blob/master/CSC-119/docs/In-Class%20Programs%2017%20-%2018/IncProg18.py)

```python
#open file in write mode 
output_file = open("data_out.txt", "w") 

#write some line to the file 
output_file.write("First line to the file") 
output_file.write("Second line to the file") 
output_file.write("Third line to the file") 

#close file 
output_file.close()
```

> :computer: Output in data_out.txt

```
First line to the file
Second line to the file
Third line to the file
```
