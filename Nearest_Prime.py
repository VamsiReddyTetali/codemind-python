def prime(n):
    c=True
    for i in range(2,(n//2)+1):
        if n%i==0:
            c=False
    return c
n=int(input())
for i in range(n):
    a=int(input())
    i=a-1
    j=a+1
    while(i):
        if prime(i):
            break
        i-=1
    while(j):
        if prime(j):
            break
        j+=1
    if prime(a):
        print(a)
    elif abs(a-i)<abs(a-j):
        print(i)
    elif abs(a-i)>abs(a-j):
        print(j)
    elif abs(a-i)==abs(a-j):
        print(i)