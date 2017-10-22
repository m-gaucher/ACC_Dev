#create a list
num_list = []

#appending  ints  into a list/print  forwards
for  num in  range (0,10):
    num_list.append(num+1)
    print("Appending  value:", num+1, "in index:", num)
    print("num_list  has", len(num_list), "items")
    
#iterate  backwards  through a list
for  num in  range(9,-1,-1):
    print("Index: ", num , "has  value: ", num_list[num])
    print("num_list  has", len(num_list), "items")
    
#retrieve a value  in a list
print("retrieve a value  in the  list: " , num_list [5] , "inindex 5")

#update a value  in a list
print("update a value  in a list: before ", num_list [0], end=", after ")
num_list [0]  = 9999
print(num_list [0])

#insert a value  in a list
num_list.insert(0, 44)
print("After  insert , index 0 now  contains  the  value: ", num_list [0]) 

#removing  value  in list
print("Removing  9999  from  num_list ...")
num_list.remove (9999)  
print("Now  num_list  contains: ",num_list)

#delete  the  list
num_list.clear ()
