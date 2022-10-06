def binarySearch(arr,value):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] > value:
            high = mid - 1
        elif arr[mid] < value:
            low = mid + 1
        else:
            return mid
    return -1 

A= [127, 220, 246, 277, 321, 454, 534, 565, 933]
# print(binarySearch(A,320))

def binarySRecursive(arr,value,low=0,high=-1):
    if len(arr)>1:
        if high==-1:
            high =len(arr)-1
        if low == high:
            if arr[low] == value:
                return low 
            else:
                return -1
        mid = (low+high)//2
        if arr[mid]>value:
            binarySRecursive(arr,value,low,mid-1)
        elif arr[mid]<value:
            binarySRecursive(arr,value,mid+1,high)
        else:
            return mid 
A= [127, 220, 246, 277, 321, 454, 534, 565, 933]
print(binarySRecursive(A,321))                 