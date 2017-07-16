# given two sorted lists l1 and l2, merge them such that the result is also sorted
# use no helper methods
# For example given l1 = [1, 2, 3] and l2 = [2, 3, 5, 10] (they can be different sizes)
# return [1, 2, 2, 3, 3, 5, 10]
# return [1, 2, 3, 5, 10]
# LINEAR TIME
# 5
def merge(l1, l2):
    i1=0
    i2=0
    merge_list=[]
    while(i1<len(l1) and i2<len(l2)):
        if l1[i1]==l2[i2]:
            merge_list.append(l1[i1])
            i1 = i1 + 1
            i2 = i2 + 1
        elif l1[i1]<l2[i2]:
            merge_list.append(l1[i1])
            i1=i1+1
        elif l2[i2]<l1[i1]:
            merge_list.append(l2[i2])
            i2=i2+1

    while(i1<len(l1)):
        merge_list.append(l1[i1])
        i1=i1+1

    while(i2<len(l2)):
        merge_list.append(l2[i2])
        i2=i2+1

    return merge_list


l1=[1,2,7]
l2=[2,3,5,10,11]

#l3=get_intersection(l1,l2)
print(merge(l1,l2))
print(merge([0,1,2,5,8,10,11],[1,2,3,5,8]))
print(merge([1,2,3,5,8],[1,2,3,5,8]))
print(merge([1,1,1,1],[2,2,2,2]))
print(merge([],[1,2,3,5,8]))
print(merge([],[]))
print(merge([1,1,1,1],[1,1,1,1]))

#print(l3)
