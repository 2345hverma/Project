
# i wnat to check whether it is toeplitz matrix or not
def istoeplitz(matrix):
	for row in range(0,len(matrix)-1):
		for column in range(0,len(matrix[row])-1):
			if matrix[row][column]!=matrix[row+1][column+1]:
				return False

	return True


matrix=[[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(istoeplitz(matrix))
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(istoeplitz(matrix))
