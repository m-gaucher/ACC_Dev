#Examples converting ints to hex
#Note: You might see notation using 0x before the hex value; we do not do this here

#create a list
hex_list = ['0','1','2','3',
            '4','5','6','7',
            '8','9','A','B',
            'C','D','E','F']

num = int(input("Please enter an integer: "))

#create an empty string to hold associated hex values per operation
hex_string = ''

#iterate per base 16 operation; storing the remainder like in binary
#this time we use the remainder as an index into our hex values
while num !=0:
    hex_string += hex_list[num % 16]
    num = num // 16

#get the length of the string so we can iterate backwards
hex_str_len = len(hex_string)
#use for loop to print the hext string backwards
print("for loop using range function; iterating backwards:")
for i in range(hex_str_len-1, -1, -1):
    print(hex_string[i], end='')

#use a for loop to print the hex_string bottom to top or backwards
print("\nfor loop using list slice(puts string backwards), iterating forwards:")
for byte in hex_string[::-1]:
    print(byte, end='')

#Print the string backwards using list slice
print("\nlist slice:")
print(hex_string[::-1])