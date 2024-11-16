n=int(input())
fact=1
for i in range(1,n+1):
    if n==0:
        print(fact)
    else:
        fact *= i
print(fact)
