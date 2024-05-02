
arr=[5,10,15,12,28,1,2,8]

n=len(arr)-1
for j in range(n):
    for i in range(n):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
          
    
    n=n-1
    print(arr)
