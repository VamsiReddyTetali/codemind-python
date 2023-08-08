def pal(s):
    s1=s[::-1]
    if s==s1:
        if len(s)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")
n=int(input())
for i in range(n):
    pal(input())