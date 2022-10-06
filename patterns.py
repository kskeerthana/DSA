def triangle(n):
    k = n-1
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k-1    
        for j in range(0,i+1):
            print('* ',end="")    
        print("\r")

# triangle(5)  

def triangleInverse(n):
    k=(n-1)
    for i in range(n,0,-1):
        for j in range(1,n-k + 1):
            # print(n-k)
            print(end=" ")
        k = k-1      
        for j in range(i,0,-1):
            print('* ',end="")    
        print("\r")   
        # for j in range():
            # print(end=" ")
        # k = k-1    
        

triangleInverse(7)            

