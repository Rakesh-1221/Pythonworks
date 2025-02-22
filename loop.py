a=[]
b=[]
c=[]
for i in range(1,110):
    if i%2==0:
        a.append(i)
    elif i%5==0:
        b.append(i)
    elif i%2!=0:
        c.append(i)
print(a)
print(b)
print(c)