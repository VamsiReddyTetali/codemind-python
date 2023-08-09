n=int(input())
for i in range(n):
    a=input()
    s=input()
    for j in s:
        if s.count(j)==1:
            print(j)
            break
    else:
        print(-1)