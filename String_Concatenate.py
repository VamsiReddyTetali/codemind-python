s1=input()
s2=input()
s=s1+s2
l=list(s)
l.sort()
print("".join(map(str,l)))