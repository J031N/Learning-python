
# while loop
'''raw=1
while raw<=5:
    Value=65
    count=1
    while count<=raw:
        print(Value,end="")
        Value+=1 
        count+=1
    print() 
    
    raw+=1  

# for loop
raw=0
col=0
for i in range(5):
   
    for j in range(raw):
        print(col,end="")
    col+=1
    print()
    raw+=1  


word='pailagam'
count=len(word)
for r in range(len(word)):
    for i in range(count):
        print(word[i],end='')
        
    print()
    count=count-1

word='pailagam'
a=5
raw=0
length=len(word)
while raw<=a:
    col=0
    while col <length:
        print(word[col],end='') 
        col=col+1

    print()
    length=length-1
    raw+=1    
    





b=int(input())
letters=b
ash=1
star=1
for i in range(b):
    for k in range(letters):
        print(chr(letters+64),end="")
    for m in range(ash):
        print(chr(i+65),end="") 
    for j in range(star):
        print("j",end='')    
    print()
    star+=1
    ash=ash+1
    letters-=1    '''



for j in range(0,5):
    for i in range(5,j,-1):
        print("*",end="")
    print()