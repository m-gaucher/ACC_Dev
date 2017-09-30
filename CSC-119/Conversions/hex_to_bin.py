#Examples of hex to bin conversion

hex_num = input("Please enter a hex value (without 0x prefix): ")

#Make the string all capitalized for simplicity
hex_num.upper()

bin_num = ''

for value in hex_num:
    if (value == '0'):
        bin_num += '0000'
    if (value == '1'):
        bin_num += '0001'
    if (value == '2'):
        bin_num += '0010'
    if (value == '3'):
        bin_num += '0011'
    if (value == '4'):
        bin_num += '0100'
    if (value == '5'):
        bin_num += '0101'
    if (value == '6'):
        bin_num += '0110'
    if (value == '7'):
        bin_num += '0111'
    if (value == '8'):
        bin_num += '1000'
    if (value == '9'):
        bin_num += '1001'
    if (value == 'A'):
        bin_num += '1010'
    if (value == 'B'):
        bin_num += '1011'
    if (value == 'C'):
        bin_num += '1100'
    if (value == 'D'):
        bin_num += '1101'
    if (value == 'E'):
        bin_num += '1110'
    if (value == 'F'):
        bin_num += '1111'

print("Hex:", "0x"+hex_num, "is", bin_num, "in binary")