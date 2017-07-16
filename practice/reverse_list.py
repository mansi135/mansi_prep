def reverse_list(new_list):
    n = len(new_list)
   # j = 0
    for i in range(n - 1, int(n /2-1), -1):
        temp = new_list[n-i-1]
        new_list[n-i-1] = new_list[i]
        new_list[i] = temp
        #j = j + 1
    print(new_list)
    return None

new_list=['a','z','e','p','c']
reverse_list(new_list)
new_list=[1,2,3,4]
reverse_list(new_list)
new_list=['aihf','zojwer','whrl','pool']
reverse_list(new_list)
new_list=[4,6,3,2,9,0,1]
reverse_list(new_list)
new_list=[]
reverse_list(new_list)


