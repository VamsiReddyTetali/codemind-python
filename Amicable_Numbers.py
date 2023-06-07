def fun(n):
    s=0
    for i in range(1,(n//2)+1):
        if n%i==0:
            s+=i
    return s
a=int(input())
b=int(input())
x=fun(a)
y=fun(b)
if a==y and b==x:
    print("Amicable")
else:
    print("Not Amicable")