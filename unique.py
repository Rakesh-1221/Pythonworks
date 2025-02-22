l1=[1,2,3,4,5,6,7,8,9,9,10,10]
l2=[]
l3=[]
for i in range(len(l1)):
    count=0
    for j in range(len(l1)):
        if l1[i]==l1[j]:
            count +=1
    if count==2 and l1[i] not in l2:
        l2.append(l1[i])
    if count==1:
        l3.append(l1[i])
print(l2,"the two repeating elements")
print(l3,"are the unique elements in the list")
print(len(l3),"is the count of unique elements")





