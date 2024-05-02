
import random
'''age=int(input("Enter your Age:")) 


if age>5:
    nationality=input("Enter your nationality:")
    if not nationality.upper()=="INDIAN":
        print("your eligible for the nationality")
    else:
        print("you are not eligibloe fotr the nationality")  
else:
    print("your age critiria not met")

    



hii=input("enter a word ")  
hello=sorted(hii)   
print(hello[1]) 




a=str(input("enter a first number"))
b=str(input("enter a second number"))
c=str(input("enter a third number"))

if sorted(a) == sorted(b) and sorted(c):
    print("all are equal")
else:
    print("not same")


values=('jobin','jose','avil','ashina')
obj=(sorted(values))


for i in range(5):
  print("*"*i)'''

mind=random.randint(1,10)
number_not_found=1

while number_not_found==1:
    guess=int(input('Enter a number:'))
    if guess==mind:
        print("Guess is corect")
        number_not_found=0
    else:
        print("not correct")    
