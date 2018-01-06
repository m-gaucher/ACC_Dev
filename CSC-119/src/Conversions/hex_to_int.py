#Examples of hex to int conversion

hex_num = input("Please enter a hex value (without 0x prefix): ")

#Make the string all capitalized for simplicity
hex_num.upper()

int_num = 0
hex_exp = len(hex_num)-1

#simplify base conversion by use of built in int()
for value in hex_num:
    int_num += int(value,16)*(16**hex_exp)
    hex_exp -= 1

print("Hex:", "0x"+hex_num, "is", int_num)
