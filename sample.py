# sample = "Hello I am ( Sunderamurthy ) I know (Java little ( Bit )"

# sample =sample.split(' ')
# # temp = '('
# # temp = sample.index('(')
# sample_list =[]
# print(sample)
# start_tracking = False
# sundera =""
# for s in sample:
#     # if '(' or ')' is s:
#     #     check = True
#     #     if(check):
#     #         print("check is true")
#     #         sample_list =  sample_list.append(s)
#     # 
#     #         print(sample_list)    

#     if s is '(':
#         sundera =""
#         start_tracking = True
#     elif s is ')':
#         start_tracking = False
#         # print(sundera)
#         sample_list.append(sundera)
    
#     elif(start_tracking):
#         sundera = sundera+s

# for s in sample_list:
#     print(s)


# # To do :
# # s=[]
# # number = [1,5,6,8,8,8,0,1,1,0,6,5]
# # for i,j in number:
# #     if i == j+1:abcabcbb

def lengthOfLongestSubstring(s):
    seen, n = set(), len(s)
    right, res = -1, 0
    for left in range(n):
        print(left, s[right+1], s[left: right+1], seen)
        while right + 1 < n and s[right+1] not in seen:
            right += 1
            seen.add(s[right])
        res = max(res, right - left + 1)
        print( s[left: right+1])
        if right == n - 1:
            break
        seen.discard(s[left])
    print(res)    
    return res
    
print(lengthOfLongestSubstring("156888011065"))




# arr = {} #empty dictionary
# for i in range(len(nums)): 
#   difference = target - nums[i] #loop to check the differnce for each indeces
#   if difference in arr: #if the difference no will be present in the dictionary
#      return [arr[difference], i] #it will return the indexes for the target sum
#   arr[nums[i]] = i