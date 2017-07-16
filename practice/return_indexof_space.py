 # Given a string s, and an index i, return the index of the
# space, or end of string, that terminates the word starting at s[i]. For example given
# s = "monkey ate my banana", i = 0, returns 6. And i = 14 (returns 20)
# 1

def return_index(s,i):
    for j in range(i,len(s)):
        if s[j]==" ":
            return j
            break
        elif j==len(s)-1:
            return j+1
            break


print(return_index("monkey ate my banana",11))
