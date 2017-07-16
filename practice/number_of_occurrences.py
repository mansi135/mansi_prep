#print the number of occurences of each element
'''
def count_occurrences(l):
    new ={}
    for i in l:
        new[i]=new[i]+1 if i in new else 1
    print(new)

count_occurrences([1, 1, 2])
count_occurrences([1])
count_occurrences([])
count_occurrences([1,2,4,7,7,1,1,10,10,9,9,3])
count_occurrences([1, 2, 3, 3])
'''

##############################################################################
#print collection of indices-method1
def print_indices(l):

   new = list(set(l))
   d={}

   for i in range(len(new)):
        indexes = [indx for indx,elem in enumerate(l) if elem ==new[i]]
        print(indexes)
        d[new[i]] = indexes

   print(d)

#print collection of indices-method2
def count(l):
    n={}
    for i in range(len(l)):
        a=l[i]
        if a in n:
            n[a].append(i)
        else:
            n[a]=[i]
    print(n)
   # return n

count([1,2,4,7,7,1,1,10,10,9,9,3])
