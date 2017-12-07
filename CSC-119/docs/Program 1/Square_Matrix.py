# declare 2d square list (5x5)
sq_matrix = [[0, 1, 2, 3, 4 ], 
	         [5, 6, 7, 8, 9 ],
	         [10,11,12,13,14], 
	         [15,16,17,18,19], 
	         [20,21,22,23,24]]
	         
print("sq_matrix dimensions")
print("num of rows:", len(sq_matrix))
print("num of columns:", len(sq_matrix[0]))

for i in range(len(sq_matrix)):
    for j in range(len(sq_matrix[i])):
        print(format(sq_matrix[i][j], "<2"), end=' ')
    print()

#print first row
print("\nPrint first row:\n")
for i in range(len(sq_matrix[0])):
    print(sq_matrix[0][i], end=' ')
print()
    
#print first column
print("\nPrint first column:\n")
for i in range(len(sq_matrix[0])):
    print(sq_matrix[i][0])

#print last row
print("\nPrint last row:\n")
for i in range((len(sq_matrix))):
    print(sq_matrix[len(sq_matrix)-1][i], end=' ')
print()

#print last col
print("\nPrint last col:\n")
for i in range(len(sq_matrix)):
    print(sq_matrix[i][len(sq_matrix)-1])
print()
