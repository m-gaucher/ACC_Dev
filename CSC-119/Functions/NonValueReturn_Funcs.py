#non-value returned functions

'''
avg_ints: return the average of 3 ints
'''
def displayPrompt():
    print("Welcome to the Program")
    print("----------------------")
    print("Description: Random words")

'''
appendLimbo: appends random strings to var passed in
'''
def appendLimbo(word):
    print("Entering appendLimbo(); word is:", word)
    word += "rando1"
    print("Inside appendLimbo(); after append word is:", word)
    word += "rando2"
    print("Inside appendLimbo(); after append word is:", word)
    print("Leaving appendLimbo()...")
    
'''
incrementLimbo: increment var passed in by 1 per increment call
'''
def incrementLimbo(num):
    print("Entering incrementLimbo(); num is:", num )
    num += 1
    print("Inside incrementLimbo(); incrementing num; num is: ", num)
    num += 1
    print("Inside incrementLimbo(); incrementing num; num is: ", num)
    print("Leaving incrementLimbo()")

'''
main: main entry point of program
'''
def main():
    print("Entering main function")
    print("Calling displayPrompt()...")
    displayPrompt()
    print("After displayPrompt() call")

    num = 0
    print("Before calling incrementLimbo; num is:", num)
    incrementLimbo(num)
    print("After calling incrementLimbo; num is:", num)

    word = "Bird"
    print("Before calling appendLimbo(); word is: ", word)
    print("Calling appendLimbo()...")
    appendLimbo(word)
    print("After calling appendLimbo(); word is:", word)

if __name__ == "__main__":
    main()
