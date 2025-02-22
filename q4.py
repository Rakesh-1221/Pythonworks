tp=(1,2,3,4,5,6,7,8,9,10)
print(tp)
tn=list(tp)
for i in range(len(tn)):
    if tn[i]%7==0:
        tn[i]='%'
    elif tn[i]%2==0:
        tn[i]='@'
tp=tuple(tn)
print(tp)
