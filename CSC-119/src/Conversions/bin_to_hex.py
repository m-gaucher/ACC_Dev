#Example of bin to hex
#refer here http://www.wikihow.com/Convert-Binary-to-Hexadecimal for algorithm


#create a list to look up hex vales
hex_list = ['0','1','2','3',
            '4','5','6','7',
            '8','9','A','B',
            'C','D','E','F']

bin_num = input("Please enter a binary number:")

#to make the iterations easier, pad up to next full nibble (4 bits)
if (len(bin_num) % 4 != 0):
    bin_num = ('0' * (4-(len(bin_num) % 4))) + bin_num
print(bin_num)

#alternative way to pad using list slice
#if (len(bin_num) % 4 != 0):
#    bin_num = bin_num[::-1]
#    bin_num += '0' * (4-(len(bin_num) % 4))
#    bin_num = bin_num[::-1]

nibble_ops = len(bin_num) / 4
hex_string = ''
nibble_sum = 0
i = 0
while nibble_ops != 0:
    nibble_sum += int(bin_num[i])   * (2**3)
    nibble_sum += int(bin_num[i+1]) * (2**2)
    nibble_sum += int(bin_num[i+2]) * (2**1)
    nibble_sum += int(bin_num[i+3]) * (2**0)
    hex_string += hex_list[nibble_sum]
    i += 4
    nibble_ops -= 1
    nibble_sum =0

print("binary: ", bin_num,"is", "0x" + hex_string, "in hexidecimal")



