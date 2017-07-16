# Print the first n fibonacci numbers.
# The numbers are defined as:
# a_1 = 1
# a_2 = 1
# a_n = a_{n-1} + a_{n-2}

def fibonacci(n):
    if n<3:
        print("Invalid entry")
    elif n>=3:
        l=[1,1]
        for k in range(2,n,1):
            l.append(l[k-1]+l[k-2])
        return l


print(fibonacci(8))
