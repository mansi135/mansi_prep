# Find two indices i, j in the list (that may be the same) such that l[i] + l[j] == n
# Return that as a tuple

def find_two_nums_summing(l, n):
	t=()
	for i in range(len(l)):
		for j in range(i,len(l),1):
			if l[i]+l[j]==n:
				t+=(i,j)
	return t

print(find_two_nums_summing([1,2,3,4,3],7))