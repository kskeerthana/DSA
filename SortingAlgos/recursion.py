def Getsum(arr):
    count = 0
    if len(arr) == 0:
        # print('List Empty')
        return 0
    else:
        return arr[0] + Getsum(arr[1:])
    # prprint(total)
        
# print(Getsum([2,4,6,5]))

def getCount(arr):
    count = 0
    if arr:
        return 1 + getCount(arr[1:])
    else:
        return 0    
# print(getCount([2,4,6,5]))       

def getMax(arr):

    if arr:
        maxm = getMax(arr[1:])
        return maxm if maxm > arr[0] else arr[0]
    else:
        return 0    
print(getMax([2,4,6,5]))           