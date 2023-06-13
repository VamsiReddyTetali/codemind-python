def prime(n):
    c=True
    for i in range(2,(n//2)+1):
        if n%i==0:
            c=False
            break
    return c
a=int(input())
b=int(input())
c=a+b
x=c+1
while(x):
    if prime(x):
        break
    x+=1
print(x-c)