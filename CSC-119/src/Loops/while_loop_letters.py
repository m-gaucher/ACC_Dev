#Examples of while loops using letters aka strings

#get string to iterate through
word = input("Please enter a string to iterate:")

print("\nFirst while loop iterating forward.")
i = 0
while i < len(word):
    print("Letter : ", word[i])
    i += 1

print("\nSecond while loop iterating forward.")
j = 0
while j != len(word):
    print("Letter : ", word[j])
    j += 1

print("\nThird while loop iterating forward.")
k = 0
while True:
    print("Letter : ", word[k])
    k += 1
    if ( k == len(word) ):
        break

print("\nFirst while loop iterating backwards.")
i = len(word)-1
while i > -1:
    print("Letter : ", word[i])
    i -= 1

print("\nSecond while loop iterating backwards.")
j = len(word)-1
while j != -1:
    print("Letter : ", word[j])
    j -= 1

print("\nThird while loop iterating backwards.")
k = len(word)-1
while True:
    print("Letter : ", word[k])
    k -= 1
    if ( k == -1 ):
        break


