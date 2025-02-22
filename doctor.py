total=0
l1=[]
for i in range(2):
    n=input("enter the name:")
    age=int(input("Enter the age:"))
    l1.append(age)
    if age<17:
        print('Fee is 200')
        total+=200
    elif age>40:
        print('Fee is 300')
        total+=300
    else:
        print('Fee is 400')
        total+=400
print(total,"is the total earnings")
print(l1)

