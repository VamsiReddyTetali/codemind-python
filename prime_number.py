n=int(input())
c=True
for i in range(2,(n//2)+1):
    if n%i==0:
        c=False
        break
if c:
    print("prime")
else:
    print("not a prime")