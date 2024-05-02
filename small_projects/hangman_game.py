

from random import randint

value = ['apple', 'house', 'basket', 'catwalk', 'mankind',
         'computer', 'phone', 'table', 'chair', 'lamp',
         'dog', 'cat', 'bird', 'fish', 'horse',
         'red', 'blue', 'green', 'yellow', 'orange',
         'tree', 'flower', 'grass', 'rock', 'river',
         'sun', 'moon', 'star', 'cloud', 'rain',
         'summer', 'winter', 'spring', 'fall', 'season',
         'happy', 'sad', 'angry', 'excited', 'calm',
         'music', 'dance', 'sing', 'play', 'instrument',
         'book', 'novel', 'poem', 'story', 'fable',
         'ocean', 'sea', 'beach', 'sand', 'wave',
         'mountain', 'valley', 'hill', 'plain', 'plateau',
         'city', 'town', 'village', 'street', 'road',
         'car', 'bus', 'train', 'bicycle', 'motorcycle',
         'airplane', 'boat', 'ship', 'submarine', 'rocket',
         'food', 'fruit', 'vegetable', 'meat', 'bread',
         'water', 'juice', 'milk', 'tea', 'coffee',
         'school', 'teacher', 'student', 'classroom', 'lesson']


random=randint(0,len(value)-1)

word=value[random]


guesses=''



turns=10
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char,end="")

        else:
            print("_ ",end="") 
            failed+=1

    if failed==0:
        print("\nYou won")
        break
    print()

    guess=input("enter a word: ")
    guesses=guesses+guess

    if guess not in word:
        turns-=1
        print("wrong")
        print('you have ',turns, 'more guesses')
        if turns==0:
            print("You are failed")
            print('The answer is:',word)

