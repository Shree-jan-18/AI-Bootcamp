A = [
	[1, 2],
	[3, 4]
]

B = [
	[5, 6],
	[7, 8]
]

add_res = [[0, 0], [0, 0]]
sub_res = [[0, 0], [0, 0]]
mul_res = [[0, 0], [0, 0]]

# addition and subtraction
for i in range(len(A)):
	for j in range(len(A[0])):
		add_res[i][j] = A[i][j] + B[i][j]
		sub_res[i][j] = A[i][j] - B[i][j]

# multiplication
for i in range(len(A)):
	for j in range(len(B[0])):
		for k in range(len(B)):
			mul_res[i][j] += A[i][k] * B[k][j]

print("A + B:")
for row in add_res:
	print(row)

print("\nA - B:")
for row in sub_res:
	print(row)

print("\nA * B:")
for row in mul_res:
	print(row)

