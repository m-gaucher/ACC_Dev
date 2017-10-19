#create an empty basestring
word = ""

#assign a string a value from user input
word = input("Please enter a string: ")

#ensure we don't compare word to a list of capitial letters
word_lower = word.lower()

#Recall how we determined odds/evens on a sequential increasing list of ints starting at 0
eoth_cap_string = ""
temp_character = ''
for index in range(len(word)):
    temp_character =  word[index] 
    if( index % 2 == 0):
        print("index: ", index, "value: ", word[index])
    else:
        temp_character = word[index].upper()
        print("index: ", index, "value: ", temp_character )
        try:
            word[index] = temp_character
        except TypeError:
            print("Cannot assign", word[index], "to: ", temp_character, "(*Strings are immutable*)"  )
    eoth_cap_string += temp_character
        
print("\nword: ", word, "; has length:", len(word))
print("\neoth cap word: ", eoth_cap_string, "; has length:", len(word))
print("\ncap word: ", word.upper(), "; has length:", len(word.upper()))

#Let's remove the capitalized letter(s) using
removed_c_word =  ""
for index in range(len(word)):
    if(eoth_cap_string[index].isupper() == False):
        removed_c_word += eoth_cap_string[index]
        
print("\nremoved cap word: ", removed_c_word, "; has length:", len(removed_c_word))

#compare the lengths of each string using len()
if ( len(word) == len(removed_c_word) ):
    print("\n", word, "has the same number of letters as", removed_c_word)
elif( len(word) > len(removed_c_word) ):
    print("\n", word, "has MORE letters than", removed_c_word)
else:
    #this case will never get hit because of above restraints
    print("\n", word, "has LESS letters than", removed_c_word) 
