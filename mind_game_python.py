import random
mind=int(random.randint(1,10))
number_not_found=1
while number_not_found:
    guess=int(input("Guess one number betwen 1 and 10:"))
    if guess==mind:
        print("your Guessed numbers is correct")
        number_not_found=0
        break
    elif guess>mind:
        print("your guessed number is more\n try again")
    else:
        print("guessed number is less")



   
      

    
    











