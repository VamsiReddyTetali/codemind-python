n=input()
l=list(map(int,input().split()))
k=int(input())
l1=[]
for i in l:
    if i+k>=max(l):
        l1.append(True)
    else:
        l1.append(False)
for i in l1:
    print(i,end=' ')