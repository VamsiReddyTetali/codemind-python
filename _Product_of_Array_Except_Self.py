n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    p=1
    for j in l:
        if j==i:
            continue
        else:
            p*=j
    a.append(p)
print(*a)