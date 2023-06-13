n=int(input())
e=0
o=0
while(n):
    r=n%10
    if r%2==0:
        e+=1
    else:
        o+=1
    n//=10
if e>0 and o>0:
    print('Mixed')
elif e>0 and o==0:
    print('Even')
elif e==0 and o>0:
    print('Odd')