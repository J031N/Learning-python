
print("Basic Calculator")
repeat='Y'
while repeat=="Y":
    num1=int(input('Enter your first number: '))

    operator=input('''for Addition ->> +
    for substraction ->> -
    for multiplication ->> *
    for division ->> /               
    ''')

    num2=int(input("Enter a second number: "))


    if operator== '+':
        print(num1+num2)
    elif operator== '-':
        print(num1-num2)   

    y_or_n=input("press Y for the another calculation ")  

    repeat=y_or_n.upper() 

    if repeat!='Y':
        print('thank you')


