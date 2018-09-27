def matmul(mat1,mat2):
	
	rows1 = len(mat1)
	columns1 = len(mat1[0])
	rows2 = 1
	columns2 = len(mat2)

	if rows1 != columns2 :
		print("matrixes of wrong size, mat1 is "+rows1+"x"+columns1+", mat2 is "+rows2+"x"+columns2)
		return 
	
	mat_out = [0 for col in range(columns1)]

	for i in range(0,columns1) :
		for k in range(0,rows1):
			mat_out[i] += mat1[i][k] * mat2[k]

	return mat_out
