n=int(input())
l=list(map(int,input().split()))
maxx=0
c=0
for i in l:
    if i==1:
        c+=1
        maxx=max(maxx,c)
    else:
        c=0
print(maxx)