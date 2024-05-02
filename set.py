'''
j={"jobin",'ashina','Avil','kiran','sujith'}
k={"jobin",'vijetha','ashina','sibin','joseph_kuruvila'}

print(j&k)
print(j-k)
print(j^k)
print(j|k)
'''
j={"jobin",'ashina','Avil','kiran','sujith'}

k=frozenset(j)

print(k)
