'''number=int(input('Enter first number'))
number2=int(input('Enter second number'))
while number<number2:
    if  number<number2:
        print(number)
        number=number+2
while number>number2:
    if number>number2:
        print(number2)
        number2+=2

num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))


while  num1<=num2:
    if num1<=num2:
        square=num1*num1*num1
        print(square)
        num1+=1

a=3
b=int(input())

while a<=b:
    if a==3:
       print(a)
    c=a*3
    
    a=c
    print(c)

a=int(input())
b=int(input())



while a<=b:
    if a%7==0 and a%2==0:
        print(a)

    a+=1   

a=int(input("cbvcfycvf:"))
b=int(input("bvycveycv:"))
total=0
while a<=b:
    total=total+a
    a=a+1 
    if a==5:
        break
   
    print(total)
    


words=input("Enter any setences:")
key=0
count=0
while key < len(words):
    if not words[key] in ['a','e','i','o','u'] or  words[key] in ['A','E','I','O','U']:
       print(words[key])
       count+=1
     
    key+=1
print(count) 

number=0
while number<=5:
    print(number)
    number+=1
else:
    print("number",number)

pin=1234
not_found=1
connt=0
while not_found:
    atm=int(input("Enter your pin number"))
    if atm==pin:
        print("correct")
        not_found=0
    elif pin!=connt:
        print('your pin uumber is wrong')    
        connt+=1
        if connt==3:
            print("you have no more attemts, ccontact with bank")
            break

name=input("Enter your name")
i=0
while i<len(name):
    print(name[i],end='_')
    i=i+1

i=int(input())
k=1
while k<=10:
    print(i,"X", k, "=" ,i*k)
    k=k+1'''

sub=int(input("How many subjects you have"))

per_sub=0
total=0
total_marks=300
while per_sub<sub:
    mark=int(input("enter your subjects mark"))
    total=total+mark
    per_sub+=1
print(total)

average=int(input("Your total marks"))
print((average/total_marks)*100)