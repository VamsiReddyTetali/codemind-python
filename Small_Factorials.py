def fact(n):
    c=1
    for i in range(1,n+1):
        c=c*i
    return c
a=int(input())
for i in range(a):
    n=int(input())
    print(fact(n))