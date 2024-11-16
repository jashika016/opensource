t=int(input())
for _ in range(0,t):
    x,y=map(int, input().split())
    if y>x:
        print('0')
    else:
        print((x-y)+1)
