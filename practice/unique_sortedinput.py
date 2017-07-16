# Given a list l, return another list that is just the list of unique items in l without using
# any other helper data structures like set etc.
def uniq_list(l):
    new = []
    current = None
    for i in range(len(l)):
        if(l[i]==current):
            continue
        else:
            new.append(l[i])
            current=l[i]

    print(new)

uniq_list([1, 1, 2])
uniq_list([1])
uniq_list([])
uniq_list([1, 2, 3])
uniq_list([1, 2, 3, 3])
