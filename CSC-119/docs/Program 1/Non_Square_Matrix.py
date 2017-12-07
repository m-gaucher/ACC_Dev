# declare 2d none square list (6x5)
non_sq_matrix = [['a', 'a', 'a', 'a', 'a'], 
	         ['s', 's', 's', 's', 'a'], 
	         ['s', 's', 's', 's', 's'], 
	         ['s', 's', 's', 's', 'a'], 
	         ['s', 's', 's', 's', 'a'],
	         ['r', 'r', 'z', 'z', 'z']]
	             
print("non_sq_matrix dimensions")            
print("num of rows:", len(non_sq_matrix))
print("num of columns:", len(non_sq_matrix[0]))

#print 2d non-sq list	
for i in range(len(non_sq_matrix)):
    for j in range(len(non_sq_matrix[i])):
        print(non_sq_matrix[i][j], end=' ')
    print()

#print first row
print("\nPrint first row:\n")
for i in range(len(non_sq_matrix[0])):
    print(non_sq_matrix[0][i], end=' ')
print()
    
#print first column
print("\nPrint first column:\n")
for i in range(len(non_sq_matrix[0])):
    print(non_sq_matrix[i][0])

#print last row
print("\nPrint last row:\n")
index_last_row = len(non_sq_matrix)-1
for i in range((len(non_sq_matrix[index_last_row]))):
    print(non_sq_matrix[len(non_sq_matrix[0])][i], end=' ')
print()

#print last col
print("\nPrint last col:\n")
index_last_col = len(non_sq_matrix[0])-1
for i in range((len(non_sq_matrix))):
    print(non_sq_matrix[i][index_last_col])
print()
