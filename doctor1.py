total=0
age=[]
for i in range(3):
        c=int(input("1.consulting\n2.exit"))
        if c==1:
            a=int(input("enter the age"))
            if a>0 and a<120:
                age.append(a)
            else:
                print("age limit is 120")
                b=int(input("enter the age"))
                age.append(b)
        if c == 2:
            break
else:
    print("Maximum limit is over")
for x in range(len(age)):
    if age[x]< 17:
        total += 200
    elif age[x]>40:
        total +=300
    else:
        total +=400
print("Total earnings is ",total)