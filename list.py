'''
a=[1,20,30,40,"a"]
b=["a","b","c",125]
c=[[a],[b]]
k=0
for i in c:
    for j in i:
        print(j)
    k+=1
    print()




a=[1,2,3,4]
b=[100,200,300,400]
c=[a,b]   
k=0

while k<len(c):
    j=0
    while j<len(c[k]):
        print(c[k][j])
        j+=1
    
    print()
    k+=1



HRNames=['Jobin',"Jvil",'Ashina','Madhavi','Yamuna','Kaveri']
TesterNames=['Jose','Kiran','meeana','Ganga','Sridevi','vijay']
Developers=['Jobin_joseph','Abhishek','Swathi','Sowmya',"Zeebra"]

Employees=[HRNames,TesterNames,Developers]
no_employees=0
while no_employees < len(Employees):
    worker=0
    letter=0
    while worker<len(Employees[no_employees]):
        if no_employees==0 and worker==3:
            Employees[no_employees][worker]=12354
            print(Employees[no_employees][worker])
        else: 
            print(Employees[no_employees][worker])
             
        worker+=1
     
    print()
    no_employees+=1
   

number=int(input("Tell your number"))

squares=[]

for i in range(1,number+1):
    squares.append("*")
    
    print(squares)

list=[12,25,"10",65,41,[1,2,3,4,5]]

list.insert(0,100)
print(list)


students=int(input("How many students in our college: "))
student_list=[]

for student in range(students):
    name=input('Enter your name')
    age=input('age')
    percenntage=input('percentage')
    student_list.append(name)
    student_list.append(age)
    student_list.append(percenntage)
print(student_list)    

count=1
for data in student_list:
    if count%3==0:
        if int(data)>75 and int(data)<100:
            print(data)
            print(student_list[count-3] ,":", student_list[count-2])
    count+=1 




squares=[]

for i in range(10):
    squares.append(i*i)
print(squares)    
 
cube=[i*i  for i in range(10)]
print(cube)


fruits=['apple','banana','orange','kiwi','apple','banana','apple']
k=fruits.count('apple')
print(fruits)
print(k)

fruits.reverse()
if fruits.count('apple')>1 and fruits.count('apple')<len(fruits):
    fruits.remove('apple')
    print(fruits)
print(k)'''







