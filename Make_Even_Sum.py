n=input()
l=list(map(int,input().split()))
c=0
if sum(l)%2==0:
    c+=1
print(c)