import time


class Sort:
    def __init__(self):
        self.values = []

    def bubble(self,listData):
        start = time.time()
        swapped = 1
        for i in range(len(listData)-1,0,-1):
            if(swapped == 0):
                return    
            swapped = 0    
            for num in range(i):
                if listData[num]>listData[num+1]:
                    listData[num],listData[num+1]=listData[num+1],listData[num]
                    swapped=1
        end = time.time()    
        time_taken = end - start 
        try:
            print(time_taken)  
        except Exception as e:
            print('time not shown because',e)          
sort = Sort()
listData = [10,4,43,5,57,91,45,9,7]
sort.bubble(listData)
print(listData)                       