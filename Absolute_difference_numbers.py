n,x=map(int,input().split())
l=[]
for i in str(n):
    l.append(i)
a=l[0:x]
b=l[-x:]
c=''.join(map(str,a))
d=''.join(map(str,b))
print(abs(int(c)-int(d)))