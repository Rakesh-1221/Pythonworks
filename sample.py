x=['abc','aba','aa','asdfa']
count=0
for i in x:
    if len(i)>2 and i[0]==i[-1]:
        print(i)
        count+=1
print(count)