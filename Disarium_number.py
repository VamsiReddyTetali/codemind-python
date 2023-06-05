n=int(input())
l=[]
for i in str(n):
    l.append(int(i))
s=0
a=1
for i in range(len(l)):
    s=s+l[i]**a
    a+=1
print(n==s)