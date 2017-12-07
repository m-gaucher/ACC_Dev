
# declare 2d jagged list (5x5)
jagged_matrix = [[0, 1, 2, 3, 4 ], 
	         [5, 6, 7],
	         [8, 9,10,11], 
	         [12], 
	         [13,14],
	         [15,16,17,18,19,20]]

print("non_sq_matrix dimensions")            
print("num of rows:", len(jagged_matrix))

print("\nLoop using range to control iteration\n")
for i in range(len(jagged_matrix)):
    print("row", i+1, ":", end=' ')
    for j in range(len(jagged_matrix[i])):
        print(format(jagged_matrix[i][j], "<2"), end =' ')
    print()

print("\nLoop using foreach mechanism to control iteration\n")
i = 1
for row in jagged_matrix:
    print("row", i, ":", *row, end=' ')
    print()
    i += 1

#print first row
print("\nPrint first row:\n")
for i in range(len(jagged_matrix[0])):
    print(jagged_matrix[0][i], end=' ')
print()

#print first column
print("\nPrint first column:\n")
for i in range(len(jagged_matrix)):
    print(jagged_matrix[i][0])

#print last row
print("\nPrint last row:\n")
last_row_ind = len(jagged_matrix) -1
for i in range(len(jagged_matrix[last_row_ind])):
    print(format(jagged_matrix[last_row_ind][i], "<2"), end =' ')
print()

#print last column; we assume each last element in a row is the last column
print("\nPrint last column (ish):\n")
for i in range(len(jagged_matrix)):
    #use some python indexing tricks :)
    print(jagged_matrix[i][-1])
