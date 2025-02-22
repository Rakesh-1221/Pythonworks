import random
c=random.randint(1,10)
for i in range(3):
    a=int(input('Enter the number'))
    if a==c:
        print('success')
        print("The random number is", c)
        break
    elif a>c:
        print('greater value')
    elif a<c:
        print('low value')
else:
    print("The random number is",c)
    print('you lost')