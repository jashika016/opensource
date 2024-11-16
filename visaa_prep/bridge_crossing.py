x,y,z = map(int, input().split())
if z<y:
    print("0")
else:
    mangoes = (z-y)//x
    print(mangoes)
