j=int(input("How much numbers you want: "))
list=[]
for i in range(1,j,7):
    list.append(i)
print(list)

search_no=int(input("Enter your number: "))

num=0
flag=0
while num < len(list):
    if list[num]==search_no:
        flag=1
        break
    num+=1  
if flag==1:
    print("your entered number is",list[num],'and the position is',num+1)
else:
    print("not found")
        






 