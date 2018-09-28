def matmul(mat1,mat2):

	rows1, cols1, rows2, cols2 = len(mat1), len(mat1[0]), len(mat2), len(mat2[0])

	if cols1 != rows2 :
		print( "matrixes of wrong size, mat1 is {}x{}, mat2 is {}x{}".format(rows1, cols1,rows2,cols2))
		return
	mat_out = [[sum(a*b for a,b in zip(mat1_row, mat2_col)) for mat2_col in zip(*mat2)] for mat1_row in mat1]

	return mat_out
