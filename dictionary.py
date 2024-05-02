

'''k={"jobin":"good man","Avil":'charismatic','Ashina':'beautiful'}

j=0
for i in k:
    if j==len(k)-1:
        k['Ashina']="cutenss"
     
    j=j+1
    print(type(k.keys()) )

    


k={"jobin":"good_man","Avil":'charismatic','Ashina':10,'jobin':20}

#for key,value in k.items():
for i in k:
    print(i,'-->',k[i])




employee={"jobin":100,"Avil":200,"kiran":300,"Amina":400}

new_employee={}

for key,value in employee.items():
    if value>200:
        new_employee[value]=key


print(new_employee) 

employee={"zobin":300,"Avil":200,"kiran":50,"Amina":400}

for key in sorted(employee):
    print(key,':',employee[key])




employee={"zobin":300,"Avil":200,"kiran":50,"Amina":400}

total=0
for value in employee.values():
    print(value)
    total=total+value

print(total) '''

r=range(20,5,-2)
for i in r:
    print(i)






