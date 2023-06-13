a,b,c=map(int,input().split())
x=50
y=60
z=100
if a>x and b>y and c>z:
    print(10)
elif a>x and b>y:
    print(9)
elif b>y and c>z:
    print(8)
elif a>x and c>z:
    print(7)
elif a>x or b>y or c>z:
    print(6)
else:
    print(5)