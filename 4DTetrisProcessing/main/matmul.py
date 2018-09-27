def matmul(mat1,mat2):

	rows1, cols1, rows2, cols2 = len(mat1), len(mat1[0]), len(mat2), len(mat2[0])

	if cols1 != rows2 :
		#print("matrixes of wrong size, mat1 is "+rows1+"x"+columns1+", mat2 is "+rows2+"x"+columns2)
		#the one above doesn't work because you need to str the integers
		print( "matrixes of wrong size, mat1 is {}x{}, mat2 is {}x{}".format(rows1, cols1,rows2,cols2))
		return

	'''
	mat_out = [0 for col in range(columns1)]

	for i in range(0,columns1) :
		for k in range(0,rows1):
			mat_out[i] += mat1[i][k] * mat2[k]
	'''

	mat_out = [[sum(a*b for a,b in zip(mat1_row, mat2_col)) for mat2_col in zip(*mat2)] for mat1_row in mat1]

	return mat_out
