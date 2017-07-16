# a is a 2D matrix (array of arrays). Return true iff n exists in a
def find_element_in_matrix(a, n):
	flag=False
	for r in range(len(a)):
		for c in range(len(a[r])):
			if a[r][c] == n:
				flag= True
				break

	return flag

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(find_element_in_matrix(a, 2))
# print(len(a))
