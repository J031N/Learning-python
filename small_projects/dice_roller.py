from random import randint
roll=True
while roll:
    dice=randint(1,6)
    print(dice)

    again_roll=input("for roll again press Y or YES")
    rol=again_roll.upper()
    if rol=='Y':
        roll=True
    else:
        print('thank you')
        roll=False
      