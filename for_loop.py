'''for i in range(5,10):
  print(i+1)
'''


'''num=int(input("Enter first number")) 
num2=int(input("Enter first number")) 
total=0
total=0
for i in range(num,num2+1,6):
    total=total+i
print(total)





even=0
for i in range(1,100+1):
    if i%3==0:
       print(i)
'''

#for i in range(10,50,1):
 #   print(i)



 # palindrome
'''word=input('Enter a number')
hello=word.lower()
word2=hello[::-1]
print(hello)
if word2==hello:
    print('palindrom')
else:
    print("not palindrom")    


words="Iam the king of this world. you cant even touch. me hvy vy hg87g ug7g g7gf ug87g yug7g"

number_of_words=0

for word in words:
    if word=='.':
        number_of_words+=1
print(number_of_words+1)    
'''

word=input("Enter a characters:")
total_words=0
total_numbers=0
special_chracters=0
length=len(word)
if length <8:
    print("No, Enter more characters")
else:    
    for i in range(length):
        if (word[i]>=chr(65) and word[i]<=chr(90) or word[i]>=chr(97) and word[i]<=chr(122)) :
            total_words+=1
        

        if word[i]>=chr(48) and word[i]<=chr(57):
            
            total_numbers+=1
        if (word[i]>=chr(32) and word[i]<=chr(47) or word[i]>=chr(58) and word[i]<=chr(64) ):
            
            special_chracters+=1
            
        
    print(total_words)       
    print(total_numbers) 
    print(special_chracters)      