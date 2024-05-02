
list=[]
inpu=int(input('Enter a number: '))
for i in range(0,inpu+1,2):
    list.append(i)
print(list)

x=int(input('Find your number: '))
start=0

end=len(list)-1
print(end)
while end>=start:
    mid=start+(end-start)//2
    if list[mid]==x:
        print('The number in the list')
        break

    elif list[mid]>x:
        end=mid-1
        print("hii")

    elif list[mid]<x:
        start=mid+1
        print('hello')
else:
    print("not in the list")        

