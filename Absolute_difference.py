def prime(n):
    c=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            c=1
            break
    if c==0:
        return True
    else:
        return False
n=input()
l=list(map(int,input().split()))
p1=1
p2=1
for i in l:
    if prime(i):
        p1*=i
    else:
        p2*=i
print(abs(p1-p2))