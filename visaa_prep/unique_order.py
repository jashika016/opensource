n=int(input())
arr=list(map(int, input().split()))
a = set()
b=[]
for i in arr:
    if i not in a:
        b.append(i)
        a.add(i)
print(*b)
