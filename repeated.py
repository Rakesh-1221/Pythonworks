a=[1,2,3,4,5,6,6,7,7]
max=0
most_repeated=0
for i in range(len(a)):
    c=a.count(a[i])
    if c>max:
        most_repeated=a[i]
        max=c
if max>1:
    print(most_repeated)
else:
    print("no repeating elements")
