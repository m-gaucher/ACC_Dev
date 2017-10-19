#create an empty basestring
word = ""

#assign a string a value from user input
word = input("Please enter a string: ")

#create a list of vowels
vowels = ['a','e','i','o','u']

#ensure we don't compare word to a list of capitial letters
word_lower = word.lower()

#create variables to store count of vowels and consonants
v_count = 0
c_count = 0

for index in range(len(word)):
    if(word[index] not in vowels):
        print("index: ", index, "value: ", word[index], "- consonant -")
        c_count +=1
    else:
        print("index: ", index, "value: ", word[index], "- vowel -")
        v_count +=1
        
print("\nword: ", word, "has length:", len(word), "vowel(s):", v_count, "consonant(s):", c_count)
