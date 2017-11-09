#open file in read mode 
input_file = open("data.txt", "r") 

#read each line of the file 
for line in input_file: 
  print (line) 
  
#close file 
input_file.close()
