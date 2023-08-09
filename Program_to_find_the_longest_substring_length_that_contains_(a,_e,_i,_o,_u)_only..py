s=input()
c=0
ma=0
for i in s:
    if i in "aeiou":
        c+=1
        ma=max(c,ma)
    else:
        c=0
print(ma)