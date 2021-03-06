# Lab 5
_Prepared for: CSC-119 Students_ /
_Prepared by: Marshall Gaucher_


**Due: 10/25/17 at 11:59 PM MT**

## Part 1: STQ From Textbook
STQ = Self-Test Questions

> :blue_book: Section 5.1.3: Questions 1, 2, 3, 5, 6, 7

> :blue_book: Section 5.2.7: Questions 1, 2, 4, 5, 6, 7, 8

## Part 2: Functions
### Introduction
Recall from In Class Program 11 & 12, we used a couple forms of functions to achieve desired results for a given routine.


### Procedure

1. Prompt the user to enter the first integer
2. Prompt the user to enter the second integer
3. Write a function to determine a given number is even
4. Write a function to determine a given number is odd
5. Write a function to determine if the first integer is greater than the second integer
6. Write a function to determine if the first integer is less than the second integer
7. Write a function to determine the least common multiple of the two integers
8. Write a function to determine if a given integer is prime
9. Write a function to determine if a given integer is composite (e.g. not prime)
10. Call the even function on the first and second integer (output the results)
11. Call the odd function on the first and second integer (output the results)
12. Call the greater than function on the first and second integer (output the results)
13. Call the less than function on the first and second integer (output the results)
14. Call the least common multiple function on the first and second integer (output the results)
15. Call the prime function on the first and second integer (output the results)
16. Call the composite function on the first and second integer (output the results)

**Prime:** a positive integer that has no positive integer divisors other than 1 and itself. More concisely, a prime number is a positive integer having exactly one positive divisor other than 1, meaning it is a number that cannot be factored. (e.g. 2, 3, 5, 7, 11, 13, 17, 19, 23...etc)

**Least Common Multiple:** The smallest positive number that is a multiple of two or more numbers. (e.g 3 & 5 would have 15 as the least common multiple)

```python
import math

'''
print first n primes
'''
def print_primes(n):
    count = 2
    prime = 5
    factor = 3
    
    if(n == 1):
        print("The first prime number is 2.")
    else:
        print("The first", n ,"prime numbers are:\n")
        print(format(2,' <4'), format(3,' <5'),end='')
    
    while (count < n):
        last_factor = round((prime**(1/2))+(0.5))
        
        for factor in range(3, last_factor, 2):
            if( prime % factor == 0):
                break
        
        if(prime % factor != 0):
            count+=1
            print(format(prime,' <5'),end='')
            
            #print 10 primes per line
            if(count % 10 == 0):
                print()
        prime += 2

print_primes(100)               

```

```
The first 100 prime numbers are:

2    3    5    7    11   13   17   19   23   29   
31   37   41   43   47   53   59   61   67   71   
73   79   83   89   97   101  103  107  109  113  
127  131  137  139  149  151  157  163  167  173  
179  181  191  193  197  199  211  223  227  229  
233  239  241  251  257  263  269  271  277  281  
283  293  307  311  313  317  331  337  347  349  
353  359  367  373  379  383  389  397  401  409  
419  421  431  433  439  443  449  457  461  463  
467  479  487  491  499  503  509  521  523  541  
```


```python
import math

'''
determine if n is prime
'''
def is_prime(n):
    #dont check invalid n or even integers
    if(n <= 1 or n % 2 == 0 ):
        return False
        
    #check special case integers to ensure below iteration is graceful    
    if(n == 2 or n ==3):
        return True
  
    #ensure we conventionally round integers
    last_factor = round((n**(1/2)))
    
    #check all odd numbers up to the sqrt of n (limit factor checks)
    for factor in range(3, last_factor, 2):
        if( n % factor == 0):
            return False
    
    return True

```
