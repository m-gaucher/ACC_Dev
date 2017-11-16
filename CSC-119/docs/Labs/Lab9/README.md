# Lab 9
_Prepared for: CSC-119 Students_ /
_Prepared by: Marshall Gaucher_


**Due: at 11:59 PM MT**

## Part 1: STQ From Textbook
STQ = Self-Test Questions

> :blue_book: Self-Test Questions on page 346: 1, 2, 3, 4, 5

> :blue_book: Self-Test Questions on page 356: 1, 2, 3

## Part 2: Text Files / Program 1 Continued
### Introduction
Create a program to maintain a dictionary of usernames and their asso-
ciated names. For this program you need to determine what goes in blank,
and ensure the program operates gracefully.

```python
#Lab9
#This code will not run until you fill in each <blank> field with appropiate value

'''
print_dict: prints all users and their associated usernames
'''
def print_dict(<blank>):
    for <blank>, <blank> in usernames.items():
        print("user:", <blank>, "username:", <blank>)
'''
main: loop to add or verify user is within dictionay
'''
def main():
    usernames = {'John ': 'john-bird43 ', 'Jenna ': 'redcar5 '}
    
    print_dict(usernames)
    
    while True:
        # Assign a var for name
        name = input('Enter a name :')

        # Check if name is in dictionary
        if <blank> in usernames:
            print ( usernames [ name ] + ' is username of ' + name )
        else :
            #not found
            print(" User : " + name + " not found in username dicitonary ")
            #get a new username for above name
            print("Please enter a username for", name)
            uname = input()

            # assign new item to dictionary
            usernames [ name ] = <blank>
            print (" Added item :" + uname )

if __name__ == "__main__":
    main()

```

