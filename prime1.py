a=[]
n=int(input("enter the limit:"))
for i in range(1,n+1):
    m=i
    count=0
    for x in range(1,m+1):
        if m%x==0:
            count+=1
    if count==2:
        a.append(m)
print(a)
