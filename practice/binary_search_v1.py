def binary_search(arr,first,last,a):
    result="NotFound"
    if len(arr)==1:
        if a==arr[0]:
            result="Found"
    else:
        while(first<=last):
            mid=int((first+last)/2)
            if a==arr[mid]:
                result="Found"
                break
            elif a < arr[mid]:
                last=mid-1
                result=binary_search(arr,first,last,a)
            elif a > arr[mid]:
                first=mid+1
                result=binary_search(arr,first,last,a)
            else:
                result="Not Found"
    return result


arr=[0,8,10,14,17]
f=0
l=len(arr)-1
print(binary_search(arr,f,l,18))