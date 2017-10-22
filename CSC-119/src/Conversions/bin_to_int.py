#In Class Program 8 Examples
bin_num = input("Enter a binary num: ")

#create a variable to sum each bit per coefficient
int_val = 0
#create a variable that starts at the highest power - 1
exponent = len(bin_num)-1

#use a for loop to iterate per bit
for bit in bin_num:
    int_val += int(bit) * (2**exponent)
    exponent -= 1

print("Binary: ", bin_num, " is ", int_val)

#Let's use a while loop to solve this
bin_num = input("Enter another binary num: ")
#create a variable to sum each bit per coefficient
int_val = 0
#create a variable that starts at the highest power - 1 (recall off by 1 topic)
exponent = len(bin_num)-1
index = 0
#use the exponent to iterate and ensure we meet the base condition
#recall which way the exponents start: high to low from left to right
while exponent != -1:
    int_val += int(bin_num[index]) * (2**exponent)
    exponent -= 1
    index += 1

print("Binary: ", bin_num, " is ", int_val)