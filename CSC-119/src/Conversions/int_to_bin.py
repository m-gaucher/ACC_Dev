# In-Class Program 7 Examples

print("Convert integer to binary using string.")
num = int(input("Please enter a integer: "))

# create empty string to hold bits
bin_num = ''

# while we have not divided the number down to 0
while num != 0:
    bin_num += str(num % 2)  # get the bit per iteration
    num = int(num / 2)  # divide the number in half or use floor division operator //

bits_length = len(bin_num)
# start at the end of the string and move backwards
# remember 0 is the starting index (read from bottom to top)
for bit in range(bits_length - 1, -1, -1):
    print(bin_num[bit], end='')  # end ='' is used to prevent printing per line

# otherwsie we can print the string backwards using list slice (Chapter 4)
print("\n")  # used to print a newline character
print(bin_num[::-1])

print("\nConvert integer to binary using a list.")
num2 = int(input("Please enter a another integer: "))
# Create an empty list
bin_num_list = []

# while we have not divided the number down to 0
while num2 != 0:
    bin_num_list.append(str(num2 % 2))  # get the bit per iteration
    num2 = int(num2 / 2)  # divide the number in half or use floor division operator //

bits_list_length = len(bin_num_list)
# start at the end of the list and move backwards
# remember 0 is the starting index (read from bottom to top)
for bit in range(bits_list_length - 1, -1, -1):
    print(bin_num_list[bit], end=' ')

# otherwsie we can print the list backwards using list slice (Chapter 4)
print("\n")  # used to print a newline character
print(*bin_num_list[::-1])
