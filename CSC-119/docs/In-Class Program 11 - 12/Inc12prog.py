#Inc12prog.py

'''
display_prompt: non-value return function with no parameters
'''
def display_prompt():
    print("Entering: ", display_prompt.__name__ + '()')
    print("Welcome to the display_prompt function!")

'''
main: main function of program
'''
def main():
    print("Program starting from: ", main.__name__ + '()')
    display_prompt()
    print("After function call, back to : ", main.__name__ + '()')

if __name__ == "__main__":
    main()
