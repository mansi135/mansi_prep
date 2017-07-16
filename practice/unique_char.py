# Given a list l, return another list that is just the list of unique items in l without using
# any other helper data structures like set etc.
def uniq_list(l):
    #new = [l[0]]
    new =[]
    for i in range(len(l)):
        flag=False
        for j in range(len(new)):
            if(l[i]==new[j]):
                flag=True
        if not flag:
            new.append(l[i])

    print(new)


def uniq_list_method2(l):
    new=[]
    for i in l:
        if i not in new:
            new.append(i)

    return new

'''
uniq_list([1, 1, 2])
uniq_list([1])
uniq_list([])
uniq_list([1,2,4,7,7,1,1,10,10,9,9,3])
uniq_list([1, 2, 3, 3])
'''

print(uniq_list_method2([1, 1, 2]))
print(uniq_list_method2([1]))
print(uniq_list_method2([]))
print(uniq_list_method2([1,2,4,7,7,1,1,10,10,9,9,3]))
print(uniq_list_method2([1, 2, 3, 3]))
