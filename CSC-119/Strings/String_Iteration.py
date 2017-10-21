#create an empty basestring
word = ""

#assign a string a value from user input
word = input("Please enter a string: ")

#print the indexes and their associated values using a for loop
print("\nPrinting string using for loop: \n")

index = 0  
for letter in word:
    print("index: ", index, "value: ", letter)
    index +=1
    
#print the indexes and their associated values using a while loop
print("\nPrinting string using a while loop: \n")

index = 0
while index < len(word):
    print("index: ", index, "value: ", word[index])
    index +=1

#print the indexes and their associated values using a for loop with range()
print("\nPrinting string using for loop with built-in range() function: \n")

for index in range(len(word)):
    print("index: ", index, "value: ", word[index])
    index +=1

#print the indexes and their associated values using a for loop with enumerate
print("\nPrinting string using for loop with built-in enumerate() function: \n")

for index, value in enumerate(word):
    print("index: ", index, "value: ", value)
