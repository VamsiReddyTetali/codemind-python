n=input()
l=[]
l.extend(n)
for i in range(len(l)):
    if l[i]=='6':
        l[i]='9'
        break
s=''.join(map(str,l))
print(s)