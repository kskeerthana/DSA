from hashlib import new
import random

# class Stack:
#     def __init__(self, Capacity=1):
#         self.top = 0
#         self.Capacity = Capacity
#         self.A = [None] * Capacity
#         # print(self.array)

#     def push(self,value):
#         # print(self.Capacity)
#         # print(self.top)
#         # print(self.A)
#         if self.Capacity == self.top:
#             print("Stack Overflow")
#             return
        
#         self.A[self.top] = value
#         self.top = self.top + 1
#         print(self.A)
        

#     def pop(self):
#         if self.top == 0:
#             print('stack underflow')

#         temp = self.A[self.top]
#         self.top = self.top - 1

#         if self.top<self.Capacity//2:
#             self.Capacity = self.Capacity//2
#             for i in range(0,self.Capacity):
#                 new_array = [None] * self.Capacity
#             self.A = new_array
#         print(temp)
#         return(temp)    


                     

# stack = Stack(5)
# for x in range(5):
#     stack.push(random.randint(1,21))

# # stack.pop()
# # for x in range(6):
# #     temp =stack.pop()
# #     if temp is not None:
# #         print(temp)    

class Stack:
    def __init__(self, Capacity=1):
        self.top = -1
        self.Capacity = Capacity
        self.A = [None] * Capacity
        # print(self.array)

    def push(self,value):
        # print(self.Capacity)
        # print(self.top)
        # print(self.A)
        if self.Capacity == self.top + 1:
            print("Stack Overflow")
            return
        self.top = self.top + 1
        self.A[self.top] = value
        # print(self.A[self.top])
        print(self.A)
        

    def pop(self):
        if self.top == -1:
            print('stack underflow')

        temp = self.A[self.top]
        self.top = self.top - 1

        if self.top<self.Capacity//2:
            self.Capacity = self.Capacity//2
            new_array = [None] * self.Capacity
            for i in range(0,self.top + 1):
                new_array[i] =self.A[i]
            self.A = new_array
        print(self.A)
        return(temp)    


                     

stack = Stack(5)
# for x in range(5):
stack.push(random.randint(1,21))

stack.pop()
# for x in range(5):
#     temp =stack.pop()
#     if temp is not None:
#         print(temp)  
  