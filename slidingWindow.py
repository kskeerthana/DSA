def getMaxSum(arr, k):
    maxSum = 0
    windowSum = 0
    start = 0
    
    for i in range(len(arr)):
        windowSum += arr[i]
        
        if ((i - start + 1) == k):
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[start]
            start += 1
    
    return maxSum

# getMaxSum([3,5,2,1,7],2)

def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')

DecimalToBinary(24)    
# https://itnext.io/sliding-window-algorithm-technique-6001d5fbe8b3