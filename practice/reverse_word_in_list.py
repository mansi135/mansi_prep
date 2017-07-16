# Given a string s that has single-space separated words like "I am a fool"
# Print the words in order, with their characters reversed
# Try not to use any helper methods like split
# For example, the result for "I am a fool" would be "I ma a loof"
# You may consider using the above helper method find_word_boundary
# 2
def reverse_words_in_list(s):

    #Method-1 which my Pogo has vetoed
    '''
    str=[]
    for word in s.split(' '):
        str.append(word[::-1])
    aa=" ".join(str)
    return aa
    '''

    #Method-2
    temp=[-1]
    for i in range(len(s)):
        if s[i]==' ':
            temp.append(i)

    temp.append(len(s))
    #print(temp)
    newstr=""

    for j in range(len(temp)-1):
        for k in range(temp[j+1]-1,temp[j],-1):
            newstr=newstr+s[k]
        newstr=newstr+' '

    return newstr

print(reverse_words_in_list("Ind am a fool"))
print(reverse_words_in_list("Two owls are making love"))
print(reverse_words_in_list("I need food all the time"))
print(reverse_words_in_list("Run at the pace of time"))