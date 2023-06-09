n=int(input())
s=n*n
re=0
while(s):
    r=s%10
    re+=r
    s//=10
if re==n:
    print("Neon Number")
else:
    print("Not Neon Number")