n=int(input())
l=list(map(int,input().split()))
s=set(l)
l1=list(s)
if len(l1)==1:
    print(l[0])
elif len(l1)==2:
    print(max(l1))
else:
    l1.remove(max(l1))
    l1.remove(max(l1))
    print(max(l1))