def fun(s):
    for i in s:
        if i in "1234567890":
            print("Yes")
            break
    else:
        print("No")
n=int(input())
for i in range(n):
    fun(input())