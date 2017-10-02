#Example of print a range of binary numbers and their int equivalent

#get a number to iterate through; unsigned values
num = int(input("Please enter a number to iterate to:"))

#while the user provides negatives values, keep prompting for valid unsigned values
while num < 0:
    num = int(input("Please enter a number to iterate to:"))

#iterate throught the range of values
print("First for loop using bin(value)")
for i in range(num):
    print("Int: ", i, " is Binary: ", bin(i))

#alternative way to print binary using format() function
str_bin_list = []
print("\nSecond for loop using format()")
for i in range(num):
    print("Int: ", i, " is Binary: ", "{0:b}".format(i))
    str_bin_list.append(str(i))


