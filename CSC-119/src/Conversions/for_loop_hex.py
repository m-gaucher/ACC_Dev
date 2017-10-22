#Example of print a range of binary numbers and their int equivalent

#get a number to iterate through; unsigned values
num = int(input("Please enter a number to iterate to:"))

#while the user provides negatives values, keep prompting for valid unsigned values
while num < 0:
    num = int(input("Please enter a number to iterate to:"))

#iterate throught the range of values using hex()
print("First for loop using hex(value)")
for i in range(num):
    print("Int: ", i, " is Hex: ", hex(i))

#alternative way to print binary using format() function
print("\nSecond for loop using format()")
for i in range(num):
    print("Int: ", i, " is Hex: ", "{0:0x}".format(i))



