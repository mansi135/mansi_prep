# Given two sorted lists, return the intersection (ie the common elements b/w the two sorted lists)
# For example given l1 = [1, 2, 3] and l2 = [2, 3, 5, 10] (they can be different sizes)
# return [2, 3]
def get_intersection(l1, l2):

    new_list = []

    if len(l1)>len(l2):
        larger_list=l1
        smaller_list=l2
    else:
        larger_list=l2
        smaller_list=l1


    for num in  larger_list:
        if num in smaller_list:
            new_list.append(num)

    return new_list

def new_method(l1,l2):
    i1=0
    i2=0
    newl3=[]
    while(i1<len(l1) and i2<len(l2)):
        if l1[i1]==l2[i2]:
            if len(newl3)==0 or l1[i1]> newl3[len(newl3)-1]:
                newl3.append(l1[i1])
            i1 = i1 + 1
            i2 = i2 + 1
        elif l1[i1]<l2[i2]:
            i1=i1+1
        elif l2[i2]<l1[i1]:
            i2=i2+1

    return newl3


l1=[1,2,3]
l2=[2,3,5,10]

#l3=get_intersection(l1,l2)
print(new_method(l1,l2))
print(new_method([0,1,2,5,8,10,11],[1,2,3,5,8]))
print(new_method([1,2,3,5,8],[1,2,3,5,8]))
print(new_method([1,1,1,1],[2,2,2,2]))
print(new_method([],[1,2,3,5,8]))
print(new_method([],[]))
print(new_method([1,1,1,1],[1,1,1,1]))

#print(l3)
