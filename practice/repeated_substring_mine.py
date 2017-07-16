# return true iff the string has a repeated substring.
# for example: "I ate not so late today" has a repeated substring ate. So it would return true for that
# but if I gave "Have not eaten", it would return false.
# 3
def has_repeated_substring(s):
    pass

import sys

def get_string(str, i, n):
	return str[i:(i+n)]

def find_match_length(str1, i1, str2, i2):
	n = 0
	while i1 < len(str1) and i2 < len(str2):
		if str1[i1] != str2[i2]:
			break
		n += 1
		i1 += 1
		i2 += 1
	return n

def find_common_substring(str, minmatch):
	ss=[]
	for i1 in range(len(str)):
		for i2 in range(i1,len(str),1):
			if i1 == i2:
				continue
			matching_length = find_match_length(str, i1, str, i2)
			if matching_length >= minmatch:
				ret=get_string(str, i1, matching_length)
				if ret not in ss:
					ss.append(ret)
			elif matching_length > 0:
				# Debug
				sys.stderr.write("Got a minmatch of %d at (%d, %d)\n" % (matching_length, i1, i2))
	#return None
	return ss

def main():
	print(find_common_substring("Hi Hello Dirty Smarty Flirty Fellow", minmatch=3))
	print(find_common_substring("I ate not so late today", minmatch=3))

if __name__ == '__main__':
	main()
