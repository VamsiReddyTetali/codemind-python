def fact(n):
    p=1
    while(n):
        p=p*n
        n-=1
    return p
n=int(input())
s=0
t=n
while(n):
    r=n%10
    a=fact(r)
    s+=a
    n//=10
if s==t:
    print("The number %d is a strong number"%(t))
else:
    print("The number %d is not a strong number"%(t))