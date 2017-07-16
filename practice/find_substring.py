# Check if the substring sub exists in s. For example, find_substring("hello buffalo", "o b") == True
# Redo- flags an partial match
def find_substring(s, sub):
    flag=False
    j=0
    for i in range(len(s)):
        if s[i]==sub[j]:
            k=i
            while j<len(sub) and k<len(s):
                if sub[j]!=s[k]:
                    j=0
                    break
                j+=1
                k+=1
                if (j+1)==len(sub):
                    flag = True
        if flag==True:
            break
        else:
            continue

    return flag

print(find_substring("hellob buffalo", "buf"))