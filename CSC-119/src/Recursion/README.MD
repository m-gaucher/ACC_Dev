# Recursion

In Chapter 11 we are introduced to a concept called Recursion. This concept allows us to solve problems using a new technique that leverages patterns/properties within solving sub-problems. Recall concepts of conditionals and control structures from earlier in the course. These will provide the foundation for understanding how recursive algorithms are designed.

First, we must understand what a “base case” is. The base case allows our recursive algorithm to gracefully terminate. Without this condition we will run into concepts of stack overflow that conceptually mirror infinite loops.  See below:

<p align ="left">
  <img width="310" height="350" src="img/recursion2.jpg">
</p>

We can define Recursion as an algorithm that calls itself one or more times until a specified condition is met, at which time the rest of each repetition is processed from the last one called to the first.

Once we understand how recursion is designed, we can transition between iterative and recursive solutions for a given problem. It is important to understand the design constraints/limitations of a given problem as recursion is not ideal for all problem sets. Remember, function calls are not free.


```python
import time
'''
This non valued function recursively decrements the parameter passed in
'''
def recr_func_decr(n):
    if n > 0:
        print(n, end=' ')
        recr_func_decr(n -1)
        
'''
This function iteratively decrements the parameter passed in
'''
def iter_func_decr(n):
    while n > 0:
        print(n, end=' ')
        n -= 1

'''
This valued return function recursively sums 0 to the parameter passed in
'''
def recr_func_dec2(n):
    #print(n)
    if n == 1:
        return 1
    else:
        #print("n:", n, "n-1", n-1)
        return n + recr_func_dec2(n -1)

'''
This valued return function recursively computes the
factorial of the parameter passed in
'''
def recr_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recr_factorial(n-1)

'''
This valued return function recursively computes the
factorial of the parameter passed in
'''
def iter_factorial(n):
    i = 2
    fact = 1
    
    if n == 0:
        return fact
    
    s = time.time()
    while i <= n:
        fact *= i
        i += 1
    e = time.time()
    print("fact:", fact)
    print("iterative factorial: ", e - s)

'''
main
'''
def main():
    #print("recr_func_decr(5):")
    #recr_func_decr(5)
    
    #print("\nsanity check base case: recr_func_decr(0)")
    #recr_func_decr(0)

    #print("\niter_func_decr(5):")
    #iter_func_decr(5)
    
    #print("\nsanity check base case: iter_func_decr(0)")
    #iter_func_decr(0)

    #print("recr_func_incr(5):")
    
    #print(recr_func_dec2(5))
    #s = time.time()
    #r = recr_factorial(950)
    #e = time.time()
    #print("r fact: ", r)
    #print("recursive factorial: ", e - s)
    
    iter_factorial(0)
    
if __name__ == "__main__":
    main()

```


