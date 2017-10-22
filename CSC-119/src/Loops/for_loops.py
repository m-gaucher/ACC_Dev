#Examples of for loops

#get a number to iterate through (assume positive numbers)
num = int(input("Please enter a number to iterate:"))

print("\nFirst for loop counting forward.")
for i in range(num):
    print("Counting : ", i)

print("\nSecond for loop counting forward.")
for i in range(0,num,1):
    print("Counting : ", i)

print("\nFirst for loop counting backwards.")
for i in range(num-1,-1,-1):
    print("Counting : ", i)

print("\nSecond for loop counting backwards.")
for i in reversed(range(num)):
    print("Counting : ", i)
