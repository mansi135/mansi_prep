# Given a list l, return another list that is just the list of unique items in l without using
# any other helper data structures like set etc.
def uniq_list(l):
    new = list(set(l))
    return new

print(uniq_list([1, 1, 2]))
print(uniq_list([1]))
print(uniq_list([]))
print(uniq_list([1, 2, 3,4,4,4,5]))
print(uniq_list([1, 2, 3, 3]))
print(uniq_list([1,2,4,7,7,1,1,10,10,9,9,3]))
