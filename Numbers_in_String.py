s=input()
c=0
for i in s:
    if i in '1234567890':
        c+=int(i)
print(c)