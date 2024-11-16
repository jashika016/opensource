n,m=map(int,input().split())
arr=list(map(int, input().split()))
c=[]
d=[]
for i in range(0,n):
    if arr[i]%m==0:
        c.append(arr[i])
    else:
        d.append(arr[i])
x=sum(c)
y=sum(d)
print(x-y)
