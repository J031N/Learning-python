from random import randint

value=['saa','boo','three']

random_number=randint(0,2)

computer=value[random_number]


player=False

while player==False:
    choice=input("enter you option: ")

    if choice==computer:
        print('Tie!')
    elif choice=='saa':
        if computer=='boo':
            print("you loose computer win")
        else:
            print("i win the match")    
    elif choice=='boo':
        if computer=='three':
            print("you loose computer ")
        else:
            print("i win the mat")    
    elif choice=='three':
        if computer=='saa':
            print("you loos")
        else:
            print("i win the") 
    else:
        print("item not matched")           
      