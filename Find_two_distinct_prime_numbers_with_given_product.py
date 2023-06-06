n=int(input())
c=0
for i in range(2,n):
    if n%i==0:
        a=i
        c=1
        break
if c:
    print(a,n//a)
else:
    print(-1)