l1=[1,2,3,4,5,6,7]
l2=[]
for i in range(len(l1)):
    if i==0 or i==2 or i==4:
        continue
    else:
        l2.append(l1[i])
print(l2)
