n=int(input())
if 3<=n<=100:
    for i in range(1,n+1):
        print('*'*i)
    for i in range(n-1,0,-1):
        print("*"*i)
else:
    print("The pattern is not possible")