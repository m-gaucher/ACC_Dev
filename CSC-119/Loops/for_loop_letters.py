#Examples of for loops with letters

#get a string to iterate through
word = input("Please enter a word to iterate:")

print("\nFirst for loop iterating forward.")
for letter in word:
    print("Letter : ", letter)

print("\nSecond for loop iterating forward.")
for i in range(0,len(word),1):
    print("Letter : ", word[i])

print("\nThird for loop iterating backwards.")
for i in word[:]:
    print("Letter : ", i)

print("\nFirst for loop iterating backwards.")
for i in range(len(word)-1,-1,-1):
    print("Letter : ", word[i])

print("\nSecond for loop iterating backwards.")
for i in reversed(range(len(word))):
    print("Letter : ", word[i])

print("\nThird for loop iterating backwards.")
for i in word[::-1]:
    print("Letter : ", i)