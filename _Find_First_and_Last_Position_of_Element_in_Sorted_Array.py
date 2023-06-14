n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in range(len(l)):
    if l[i]==k:
        print(i,end=" ")
        break
else:
    print(-1,end=" ")
for i in range(len(l)-1,-1,-1):
    if l[i]==k:
        print(i,end=" ")
        break
else:
    print(-1)