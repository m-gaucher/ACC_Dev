# create / declare a tuple
num_tuple = ()
print("num_tuple contains : ", num_tuple )
print("length of num_tuple : ", len( num_tuple ))

# declaring a tuple with ints
num_tuple = (1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10)
print("Creating a tuple of ints :", num_tuple )
print("length of num_tuple : ", len( num_tuple ))

# iterating forwards in a tuple
for num in num_tuple :
    print("Value : ",num)
    print("length of num_tuple : ", len( num_tuple ))

# print max value in tuple
print("max value in tuple is: ", max( num_tuple ))

# print min value in tuple
print("min value in tuple is: ", min( num_tuple ))

# convert tuple to list
print("num_tuple to list : ", list ( num_tuple ))

# declare a list of strings
string_list = ['chicken ','cow ','bird ','dog ','elk ']
print("string_list contains : ", string_list )
print("number of values in string_list : ", len( string_list ))
