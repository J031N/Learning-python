
subjects=['Kannada','English','Hindi','Maths','Social-Science','Accounts']

studentCount=int(input("How many students are in your college: "))

report={}
rollNumber=0
for students in range(studentCount):
    name=input("Enter student name %d: " %(rollNumber+1))
    rollNumber+=1
   

    marks=[]
    for subject in subjects:
        marks.append(int(input("Enter your marks for %s: " %(subject))))
  
    report[name]=marks 
    
    
    
    for key,value in report.items():
        total=sum(value)
        percentage=total/600
    print("%s's total marks %d"%(name,total))

    print('percentage of %s'%(name),percentage*100)

    pass_or_fail=input("Do you want to check pass or fail %s"%(name)+' Enter your yes or no: ' )

    
    if pass_or_fail=="yes":
        if total<=300:
            print('%s'%(name),'you are failed')  
        else:
            print('%s'%(name),'you are passed')
    elif pass_or_fail=="no":
        print("Thank you")
   