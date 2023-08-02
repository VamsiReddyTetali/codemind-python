n=int(input())
for i in range(n):
    n,a,b,k=map(int,input().split())
    c1=n//a
    c2=n//b
    c=n//(a*b)
    if (c1+c2-c)>=k:
        print("Win")
    else:
        print("Lose")