#value returned functions

'''
avg_ints: return the average of 3 ints
'''
def avg_ints(n1,n2,n3):
    return (n1+n2+n3) / 3.0

'''
append_letter: Appends string "B" to a given string
'''
def append_letter(word):
    word += "B"
    return word

'''
main: main entry point of program
'''
def main():
    print("Entering main function")
    average = 0
    print("Before avg_int(); average is:", average)
    print("Calling avg_int() function...")
    average = avg_ints(1,2,3)
    print("After avg_int() function; average is:", average)
    word = "Bird"
    print("Before append_letter(), word is:", word)
    print("Calling append_letter() function...")
    word = append_letter(word)
    print("After append_letter(), word is:", word)

if __name__ == "__main__":
    main()
