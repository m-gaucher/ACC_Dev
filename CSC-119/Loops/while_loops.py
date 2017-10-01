#Examples of while loops

#get a number to iterate through (assume positive numbers)
num = int(input("Please enter a number to iterate:"))

print("\nFirst while loop counting forward.")
i = 0
while i < num:
    print("Counting : ", i)
    i += 1

print("\nSecond while loop counting forward.")
j = 0
while j != num:
    print("Counting : ", j)
    j += 1

print("\nThird while loop counting forward.")
k = 0
while True:
    print("Counting : ", k)
    k += 1
    if ( k == num ):
        break

print("First while loop counting backwards.")
i = num
while i > 0:
    print("Counting : ", i)
    i -= 1

print("\nSecond while loop counting backwards.")
j = num
while j != 0:
    print("Counting : ", j)
    j -= 1

print("\nThird while loop counting backwards.")
k = num
while True:
    print("Counting : ", k)
    k -= 1
    if ( k == 0 ):
        break


