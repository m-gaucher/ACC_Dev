# Lab 2
_Prepared for: CSC-119 Students_ /
_Prepared by: Marshall Gaucher_

**Due:  at 11:59 PM MT**

## Part 1: STQ From Textbook
STQ = Self-Test Questions

> :blue_book: Section 2.1.7 (pg49): Questions 1, 3, 4, 5, 7

> :blue_book: Section 2.2.5 (pg56): Questions 1, 2, 4, 5, 6

> :blue_book: Section 2.3.3 (pg60): Questions 1, 2, 3, 4, 5

> :blue_book: Section 2.4.6 (pg66): Questions 1, 3, 4, 6

## Part 2: Programming Exercises
### Introduction
For this part of the homework, we will create a pulse wave with ASCII characters
based on the Unicode values, of each character, in your first name.

### Procedure

1. Prompt the user for their frst name (this is simply used for display purposes; nothing more)
2. Print the frst name variable
3. Prompt the user for a pulse number (this will be used later in you algorithm)
4. Print the pulse number variable
5. Print the Unicode values of each character in their first name
6. Print the sum of Unicode characters of the first name
7. Print the difference of Unicode characters in the first name
8. Print each character of the first name, per line, followed by a series ASCII characters
Series = ( Unicode value % pulse number variable )

## Hints

1. To make a pulse, use the mod(%) operator.
2. Prompt is used to indicate the system is awaiting user input, to ultimately store in a variable.
3. We can convert an int to a string via str() and we can convert a base10 string to an int via int()
Page 2

```
Please enter your first name: Frank
Frank
Please enter a pulse number: 13
13
70 114 97 110 107
Sum of Unicode values: 498
Difference of Unicode values: -358
F .....
r .............
a ......
n ......
k ...
```
