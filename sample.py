sample = "Hello I am ( Sunderamurthy ) I know (Java little ( Bit )"

sample =sample.split(' ')
# temp = '('
# temp = sample.index('(')
sample_list =[]
print(sample)
start_tracking = False
sundera =""
for s in sample:
    # if '(' or ')' is s:
    #     check = True
    #     if(check):
    #         print("check is true")
    #         sample_list =  sample_list.append(s)
    # 
    #         print(sample_list)    

    if s == '(':
        sundera =""
        start_tracking = True
    elif s == ')':
        start_tracking = False
        # print(sundera)
        sample_list.append(sundera)
    
    elif(start_tracking):
        sundera = sundera+' '+s

for s in sample_list:
    print(s)