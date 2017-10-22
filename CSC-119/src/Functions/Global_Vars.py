#global var with none-valued functions
num = 0
word = "bird"

'''
func1: Increment the global var by 1
'''
def func1():
    global num
    print("Entering func1 num is: ", num )
    num +=1
    print("Leaving func1 num is: ", num)

'''
func2: Increment the global var by 2
'''
def func2():
    global num
    print("Entering func2 num is: ", num)
    num +=2
    print("Leaving func2 num is: ", num)

'''
func3: Append the string "random1" to var word
'''
def func3():
    global word
    print("Entering func3 word is:", word)
    word += "random1"
    print("Leaving func3 word is:", word)

'''
func4: Append the string "randomnessMax" to var word
'''
def func4():
    global word
    print("Entering func4 word is:", word)
    word += "randomnessMax"
    print("Leaving func4 word is:", word)

'''
main: main entry point of program
'''
def main():
    print("Main function, num is:", num)
    print("Calling func1() from main..")
    func1()
    print("Back in main() from func1(); num is", num)
    print("Calling func2() from main..")
    func2()
    print("Back in main() from func2(); num is", num)
    print("Calling func3() from main..")
    func3()
    print("Back in main() from func3(); num is", num)
    print("Calling func4() from main..")
    func4()
    print("Back in main() from func4(); num is", num)

if __name__ == "__main__":
    main()
